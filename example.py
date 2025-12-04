from ariary import (
    AriarySDK,
    ApiConfig,
    CreatePaymentDto,
    SendSmsDto,
    BulkSmsDto,
    SendTransactionDto,
)


def main():
    # Initialiser le SDK avec les credentials
    config = ApiConfig(
        apiKey="votre_api_key",
        secretId="votre_secret_id",
        projectId="votre_project_id",
    )

    sdk = AriarySDK(config)

    try:
        # ============ EXEMPLES DE PAIEMENT ============
        print("=== Exemples de paiement ===")

        # Créer un paiement
        payment = sdk.payment.create_payment(
            CreatePaymentDto(
                code="PAY-001",
                amount=50000,
                projectId="votre_project_id",
            )
        )
        print(f"Paiement créé: {payment}")

        # Récupérer tous les paiements
        all_payments = sdk.payment.get_all_payments()
        print(f"Tous les paiements: {all_payments}")

        # Récupérer un paiement spécifique
        payment_by_id = sdk.payment.get_payment_by_id(payment.id)
        print(f"Paiement par ID: {payment_by_id}")

        # Mettre à jour le reste d'un paiement
        updated_payment = sdk.payment.update_payment_rest(payment.id, "TICKET123")
        print(f"Paiement mis à jour: {updated_payment}")

        # ============ EXEMPLES SMS ============
        print("\n=== Exemples SMS ===")

        # Envoyer un SMS à plusieurs numéros
        multi_sms = sdk.sms.send_multi_sms(
            SendSmsDto(
                phones=["261345678901", "261345678902", "261345678903"],
                message="Message à tous",
            )
        )
        print(f"SMS multiples envoyés: {multi_sms}")

        # Envoyer des SMS différents en masse
        bulk_sms = sdk.sms.send_bulk_sms(
            BulkSmsDto(
                messages=[
                    {"phones": ["261345678901"], "message": "Message 1"},
                    {"phones": ["261345678902"], "message": "Message 2"},
                    {"phones": ["261345678903"], "message": "Message 3"},
                ]
            )
        )
        print(f"SMS en masse envoyés: {bulk_sms}")

        # Récupérer l'historique des SMS
        sms_history = sdk.sms.get_sms_history()
        print(f"Historique des SMS: {sms_history}")

        # Récupérer un SMS spécifique
        if multi_sms.data and len(multi_sms.data) > 0:
            sms_by_id = sdk.sms.get_sms_by_id(multi_sms.data[0]["id"])
            print(f"SMS par ID: {sms_by_id}")

            # Mettre à jour un SMS
            updated_sms = sdk.sms.update_sms(
                multi_sms.data[0]["id"],
                {"message": "Message mis à jour"},
            )
            print(f"SMS mis à jour: {updated_sms}")

        # ============ EXEMPLES DE TRANSFERT ============
        print("\n=== Exemples de transfert ===")

        # Envoyer une transaction
        transaction = sdk.transfer.send_transaction(
            SendTransactionDto(phone="261345678901", amount=100000)
        )
        print(f"Transaction envoyée: {transaction}")

        # Récupérer toutes les transactions
        all_transactions = sdk.transfer.get_all_transactions()
        print(f"Toutes les transactions: {all_transactions}")

        # Récupérer une transaction spécifique
        transaction_by_id = sdk.transfer.get_transaction_by_id(transaction.id)
        print(f"Transaction par ID: {transaction_by_id}")

        # Mettre à jour une transaction
        updated_transaction = sdk.transfer.update_transaction(
            transaction.id,
            SendTransactionDto(phone="261345678902", amount=150000),
        )
        print(f"Transaction mise à jour: {updated_transaction}")

    except Exception as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    main()
