from django.contrib.auth.models import  BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, is_superuser=False, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        user =  self.model(
            email = self.normalize_email(email),
            name = name,
            is_superuser=is_superuser,
            
            )
        user.set_password(password),
        user.save(using=self._db)
        return user
    
    def staff_user(self, name, email, password):
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, email,  password=None):
        user = self.create_user(
            name,
            email,
            password=password,
            is_superuser=True
        )
        user.is_staff = True
        user.admin = True
        user.save(using=self._db)
        return user
    