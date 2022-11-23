from django.test import TestCase

from transactions.models import Transaction
from utils.cnab_parser import CnabParser


class TestCnabParser(TestCase):
    def test_parsing(self):
        data = CnabParser.normalize_cnab("CNAB.txt")
        CnabParser.add_to_db(data)

        self.assertEqual(len(data), Transaction.objects.all().count())
