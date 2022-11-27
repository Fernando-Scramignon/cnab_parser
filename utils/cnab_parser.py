from transactions.serializers import TransactionSerializer

from datetime import date, time
from decimal import Decimal


class CnabParser:
    @classmethod
    def normalize_str_cnab(cls, file_str: str) -> list[dict]:
        if not file_str:
            raise ValueError()

        output = []
        file_line_list = file_str.split("\n")

        for line in file_line_list:
            if not line:
                break

            transaction: dict = {}
            transaction["type"] = line[0:1]
            transaction["date"] = date.fromisoformat(line[1:9])
            transaction["value"] = round(Decimal(int(line[9:19]) / 100), 2)
            transaction["cpf"] = line[19:30]
            transaction["card"] = line[30:42]
            transaction["hour"] = time.fromisoformat(line[42:48])
            transaction["shop_owner"] = line[48:62].strip()
            transaction["shop_name"] = line[62:81].strip()

            serializer = TransactionSerializer(data=transaction)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            validated_data["type"] = validated_data["type"].type
            output.append(validated_data)

        return output

    @classmethod
    def normalize_cnab(cls, file_path) -> list[dict]:
        if not file_path:
            raise ValueError()
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
                validated_data = serializer.validated_data
                validated_data["type"] = validated_data["type"].type

                output.append(validated_data)

                line = file.readline()

        return output

    @classmethod
    def add_to_db(cls, cnab_dict: dict) -> None:
        serializer = TransactionSerializer(data=cnab_dict, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
