from django.test import TestCase
from mysite.forms import SignUpForm


class SignUpFormTest(TestCase):

    def test_title_max_length(self):
        form = SignUpForm()
        max_length = form.fields['email'].max_length
        self.assertEquals(max_length, 254)

    def test_renew_form_date_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(form.fields['email'].help_text,
                         'Required. Inform a valid email address.')
