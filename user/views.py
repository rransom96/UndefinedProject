from christmas_list.settings import STRIPE_API_KEY
from django.shortcuts import render
from django.views.generic import View
import stripe


class UserDonate(View):

    def get(self, *args, **kwargs):
        return render(self.request, "users/user_donate.html")


    def post(self, *args, **kwargs):
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = STRIPE_API_KEY

        # Get the credit card details submitted by the form
        token = self.request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
            charge = stripe.Charge.create(
            amount=1000, # amount in cents, again
            currency="usd",
            source=token,
            description="Example charge"
        )
        except stripe.error.CardError as e:
            # The card has been declined
            pass

        return render(self.request, "users/user_donate.html")
        #return HttpResponseRedirect(reverse('list_chirps'))