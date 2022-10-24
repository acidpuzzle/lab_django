import logging
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404

logger = logging.getLogger(__name__)


class CustomPaginator(Paginator):
    def get_fixed_length_page_range(self, number=1, *, on_each_side=2):
        """
        Range of fixed length pages
        [1,2,3,4,5] or [7,8,9,10,11]
        """

        number = self.validate_number(number)
        on_each_side = self.validate_number(on_each_side)

        full_length = (on_each_side * 2) + 1

        if self.num_pages < full_length:
            yield from range(1, self.num_pages + 1)
        elif number <= on_each_side:
            yield from range(1, full_length + 1)
        elif number >= self.num_pages - on_each_side:
            yield from range(self.num_pages - full_length + 1, self.num_pages + 1)
        else:
            yield from range(number - on_each_side, number + on_each_side + 1)


class ObjectMixin:
    model = None
    model_form = None
    template = None
    logger.info(f"{model=}")
    logger.info(f"{model_form=}")
    logger.info(f"{template=}")


class ObjectDetailMixin(ObjectMixin):
    def get(self, request, instance_id):
        instance = get_object_or_404(self.model, instance_id__iexact=instance_id)
        logger.info(f"{instance=}")
        return render(request, self.template, context={'instance': instance, 'model': self.model})


class ObjectListMixin(ObjectMixin):
    default_paginate_by = 3

    def get(self, request):
        instances = self.model.objects.all()
        logger.debug(f"{instances=}")

        paginate_by = request.GET.get('paginate_by', self.default_paginate_by)

        paginator = CustomPaginator(instances, paginate_by)
        page_number = request.GET.get('page', 1)
        page_instance = paginator.get_page(page_number)
        is_paginated = page_instance.has_other_pages()
        next_page = page_instance.next_page_number() if page_instance.has_next() else ''
        prev_page = page_instance.previous_page_number() if page_instance.has_previous() else ''

        page_number_gen = paginator.get_fixed_length_page_range(page_number)

        context = {
            'instance': page_instance,
            'is_paginated': is_paginated,
            'next_page': next_page,
            'prev_page': prev_page,
            'page_number_gen': page_number_gen,
            'model': self.model,
        }
        logger.info(f"{context=}")
        return render(request, self.template, context=context)


class ObjectCreateMixin(ObjectMixin):
    def get(self, request):
        form = self.model_form()
        logger.info(f"{form=}")
        return render(request, self.template, context={'form': form, 'model': self.model})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        logger.info(f"{bound_form=}")

        logger.info(f"{bound_form.is_valid=}")
        if bound_form.is_valid():
            new_instance = bound_form.save()
            logger.info(f"{new_instance=}")
            return redirect(new_instance)
        logger.info(f"{bound_form.errors}")
        return render(request, self.template, context={'form': bound_form, 'model': self.model})


class ObjectUpdateMixin(ObjectMixin):
    def get(self, request, instance_id):
        instance = self.model.objects.get(instance_id__iexact=instance_id)
        logger.info(f"{instance=}")
        bound_form = self.model_form(instance=instance)
        logger.info(f"{bound_form=}")
        return render(request, self.template, context={'form': bound_form, 'instance': instance, 'model': self.model})

    def post(self, request, instance_id):
        instance = self.model.objects.get(instance_id__exact=instance_id)
        logger.info(f"{instance=}")
        bound_form = self.model_form(request.POST, instance=instance)
        logger.info(f"{bound_form=}")

        logger.info(f"{bound_form.is_valid()=}")
        if bound_form.is_valid():
            updated_instance = bound_form.save()
            logger.info(f"{updated_instance=}")
            return redirect(updated_instance)
        return render(request, self.template, context={'form': bound_form, 'instance': instance, 'model': self.model})


class ObjectDeleteMixin(ObjectMixin):
    def get(self, request, instance_id):
        instance = self.model.objects.get(instance_id__iexact=instance_id)
        logger.info(f"{instance=}")
        return render(request, self.template, context={'instance': instance, 'model': self.model})

    def post(self, reqest, instance_id):
        instance = self.model.objects.get(instance_id__iexact=instance_id)
        logger.info(f"{instance=}")
        redirect_url = self.model.get_list_url()
        logger.info(f"{redirect_url=}")
        logger.info(f"{instance.delete()}")
        return redirect(redirect_url)
