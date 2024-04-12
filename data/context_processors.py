def user_is_expert_or_moderator(request):
    user_is_expert_or_moderator = False
    if request.user.groups.filter(name__in=['Experten', 'Moderatoren']).exists():
        user_is_expert_or_moderator = True
    return {'user_is_expert_or_moderator': user_is_expert_or_moderator}