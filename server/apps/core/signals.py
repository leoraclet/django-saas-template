from djstripe.event_handlers import djstripe_receiver
from djstripe.models import Charge, Event, PaymentMethod


# This file contains signal handlers for Stripe events using dj-stripe.
@djstripe_receiver("charge.succeeded")
def handle_charge_succeeded(sender, **kwargs):
    event: Event = kwargs.get("event")  # type: ignore
    charge_id = event.data["object"]["id"]
    charge = Charge.objects.get(id=charge_id)
    print("Charge succeeded!")
    print(f"Sender: {sender}")
    print(f"Event: {event}")
    print(f"Charge: {charge}")


@djstripe_receiver("payment_method.attached")
def handle_payment_method_attached(sender, **kwargs):
    event: Event = kwargs.get("event")  # type: ignore
    payment_method_id = event.data["object"]["id"]
    payment_method = PaymentMethod.objects.get(id=payment_method_id)
    print("Payment Method Attached!")
    print(f"Sender: {sender}")
    print(f"Event: {event}")
    print(f"Payment Method: {payment_method}")
    print(f"Payment Method: {payment_method}")
