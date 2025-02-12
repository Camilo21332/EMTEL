from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class PersonaManager(BaseUserManager):
    def create_user(self, per_documento, per_nombre, password=None):
        if not per_documento:
            raise ValueError("El documento de identidad es obligatorio")

        user = self.model(per_documento=per_documento, per_nombre=per_nombre)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, per_documento, per_nombre, password):
        user = self.create_user(per_documento, per_nombre, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

