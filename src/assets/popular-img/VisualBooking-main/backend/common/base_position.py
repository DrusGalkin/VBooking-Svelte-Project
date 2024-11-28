from users.models.position import Position

ADMIN_POSITION = Position.objects.filter(code='admin').first()
USER_POSITION = Position.objects.filter(code='user').first()
OWNER_POSITION = Position.objects.filter(code='owner').first()
