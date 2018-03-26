from rest_framework import serializers
from app.user.models import Userdetails

class userSerializer(serializers.ModelSerializer):

	class Meta:
		model=Userdetails
		#For one or few fields we use 
		# fields=('first_name','last_name')
		#For all present in user model to see as JSON we use
		fields='__all__'



		