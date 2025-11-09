from functools import wraps
from django.http import JsonResponse

def role_required(allowed_roles=[]):
    """
    Decorator to restrict access based on user role.
    allowed_roles: list of roles or 'self' / 'owner' checks
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication required'}, status=401)

            user_role = getattr(request.user, 'role', None)
            if not user_role:
                return JsonResponse({'error': 'Role not defined'}, status=403)

            # 'self' means user can access their own object (check kwargs['id'])
            if 'self' in allowed_roles and 'id' in kwargs and kwargs['id'] == request.user.id:
                return view_func(request, *args, **kwargs)

            if user_role in allowed_roles:
                return view_func(request, *args, **kwargs)

            # Custom checks for task owner, club manager, assignee can be handled in view
            return JsonResponse({'error': 'Permission denied'}, status=403)

        return _wrapped_view
    return decorator

