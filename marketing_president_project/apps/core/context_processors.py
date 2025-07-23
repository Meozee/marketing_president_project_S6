# apps/core/context_processors.py

def user_profile_context(request):
    """
    Menyediakan data user yang sedang login ke semua template.
    """
    # Pastikan user sudah login untuk menghindari error
    if request.user.is_authenticated:
        # Tentukan role berdasarkan flag
        if request.user.is_superuser:
            role = 'Superadmin'
        elif request.user.is_staff:
            role = 'Admin'
        else:
            role = 'Staff'
        
        return {
            'logged_in_user': request.user,
            'user_role': role
        }
    return {}
