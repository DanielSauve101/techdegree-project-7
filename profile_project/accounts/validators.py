import re

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class DuplicatePasswordValidator(object):
    def validate(self, password, user):
        if user.check_password(password):
            raise ValidationError(
                _("Your password must be different from old password"),
                code='password_no_change',
            )
        else:
            password_changed(password)

    def get_help_text(self):
        return _(
            "Your password must be different from old password"
        )

# code adapted from https://sixfeetup.com/blog/how-to-create-custom-password-validators-in-django
# By: Anthony Bosio


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Your password must contain at least 1 numerical digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 numerical digit, 0-9."
        )


class LetterValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]'+'[a-z]', password):
            raise ValidationError(
                _("Your password must contain at least 1 uppercase and" +
                  " 1 lowercase letter, A-Z and a-z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase and" +
            " 1 lowercase letter, A-Z and a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("Your password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )


class ContainUserNameValidator(object):
    def validate(self, password, user=None):
        if user.username in password:
            raise ValidationError(
                _("Your password may not contain the user name: "),
                code='password_contains_username',
            )

    def get_help_text(self):
        return _("Your password may not contain the user name: ")
