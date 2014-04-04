from horizon import views


class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'market/vms/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
	vm1 = {'name': 'Matlab','compute': 'Dell','storage':'HP'}
	vm2 = {'name':'Web Server','compute':'Compute','storage':'Storage'}
	context['virtualMachines'] = [vm1, vm2]
        return context
