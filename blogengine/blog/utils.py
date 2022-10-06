import logging

from django.shortcuts import render, redirect, reverse, get_object_or_404

logger = logging.getLogger(__name__)


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
    def get(self, request):
        instances = self.model.objects.all()
        print(f"{instances=}")
        logger.info(f"{instances=}")
        return render(request, self.template, context={'instances': instances, 'model': self.model})


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
