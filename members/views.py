from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Club, ClubMembership

# Add a member with role
def add_member(request, id):
    club = get_object_or_404(Club, id=id)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')

        user = get_object_or_404(User, id=user_id)

        if ClubMembership.objects.filter(user_id=user, club_id=club).exists():
            messages.warning(request, f"{user.username} is already a member of {club.name}.")
        else:
            ClubMembership.objects.create(user_id=user, club_id=club)
            messages.success(request, f"{user.username} added to {club.name} as a member successfully!")

        return redirect('club_detail', id=id)

    users = User.objects.all()
    return render(request, 'add_member.html', {'club': club, 'users': users})


# Remove a member from a club
def remove_member(request, id, userId):
    club = get_object_or_404(Club, id=id)
    user = get_object_or_404(User, id=userId)

    membership = ClubMembership.objects.filter(user_id=user, club_id=club).first()

    if membership:
        membership.delete()
        messages.success(request, f"{user.username} has been removed from {club.name}.")
    else:
        messages.warning(request, f"{user.username} is not a member of {club.name}.")

    return redirect('club_detail', id=id)


# Assign or update a member’s role in a club
def assign_role(request, id, userId):
    club = get_object_or_404(Club, id=id)
    user = get_object_or_404(User, id=userId)

    membership = ClubMembership.objects.filter(user_id=user, club_id=club).first()

    if not membership:
        messages.error(request, f"{user.username} is not a member of {club.name}.")
        return redirect('club_detail', id=id)

    if request.method == 'POST':
        new_role = request.POST.get('role_in_club')
        if new_role:
            membership.role_in_club = new_role
            membership.save()
            messages.success(request, f"{user.username}'s role updated to {new_role} in {club.name}.")
        else:
            messages.warning(request, "No role selected.")
        return redirect('club_detail', id=id)

    roles = dict(ClubMembership.MEMBER_ROLES)
    return render(request, 'assign_role.html', {'club': club, 'user': user, 'roles': roles})
# Create your views here.
