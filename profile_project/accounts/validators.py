import re

from django.contrib.auth.password_validation import password_changed
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

# code adapted from https://sixfeetup.com/blog/how-to-create-custom-password-validators-in-django
# By: Anthony Bosio


class DuplicatePasswordValidator(object):
    def validate(self, password, user=None):
        new_password = password_changed(password)
        if not password_changed():
            raise ValidationError(
                _("Your password must be different from old password"),
                code='password_no_change',
            )

    def get_help_text(self):
        return _(
            "Your password must be different from old password"
        )


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
