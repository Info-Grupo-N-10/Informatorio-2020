from django.core.exceptions import PermissionDenied

class PermisosMixin:
    rol = None
    def dispatch(self, request, *args, **kwargs):
        if check(request, self.rol):
            return super().dispatch(request, *args, **kwargs)
        else: 
            raise PermissionDenied


def check(request, rol):
    u = request.user
    if u.propietario and rol == 'propietario':
        return True
    elif not (u.propietario) and rol == 'comun':
        return True
    else:
        return False
