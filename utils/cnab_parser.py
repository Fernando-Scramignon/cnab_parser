from transactions.serializers import TransactionSerializer

from datetime import date, time
from decimal import Decimal


class CnabParser:
    @classmethod
    def normalize_cnab(cls, file_path: str) -> list[dict]:
        output = []
        with open(file_path, "r") as file:
            line = file.readline()

            while line:
                transaction_dict = {}

                transaction_dict["type"] = line[0:1]
                transaction_dict["date"] = date.fromisoformat(line[1:9])
                transaction_dict["value"] = round(Decimal(int(line[9:19]) / 100), 2)
                transaction_dict["cpf"] = line[19:30]
                transaction_dict["card"] = line[30:42]
                transaction_dict["hour"] = time.fromisoformat(line[42:48])
                transaction_dict["shop_owner"] = line[48:62]
                transaction_dict["shop_name"] = line[62:81]

                serializer = TransactionSerializer(data=transaction_dict)
                serializer.is_valid(raise_exception=True)
                output.append(serializer.validated_data)

                line = file.readline()

        return output

    @classmethod
    def add_to_db(cls, cnab_dict: dict) -> None:
        serializer = TransactionSerializer(data=cnab_dict, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
