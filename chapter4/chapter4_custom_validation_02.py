from pydantic import BaseModel, EmailStr, ValidationError, model_validator


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.password_confirmation:
            raise ValueError("Passwords don't match")
        return self


# Passwords not matching
try:
    UserRegistration(
        email="jdoe@example.com", password="aa", password_confirmation="bb"
    )
except ValidationError as e:
    print(str(e))

# Valid
user_registration = UserRegistration(
    email="jdoe@example.com", password="aa", password_confirmation="aa"
)
# email='jdoe@example.com' password='aa' password_confirmation='aa'
print(user_registration)
