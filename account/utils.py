from account.models import PbProfile,PbUserOauthToken



def save_profile_from_social(backend,user,response,*args,**kwargs):
    print(user)
    if kwargs['is_new']:
        attrs = {'user': user}

        if backend.name == "twitter":
             social_data ={
                 "first_name" : kwargs['details']['first_name'],
                 "last_name" : kwargs['details']['last_name'],


             }
        elif backend.name == "linkedin-oauth2":
             social_data ={
                 "first_name" : kwargs['details']['first_name'],
                 "last_name" : kwargs['details']['last_name'],

                 # "country" : response['location']['country']['code'],
                 # "industry" : response['industry']
                }
             PbUserOauthToken.objects.create(
                 user=user,
                 linkedin=response.get("access_token"),
             )
        elif backend.name == "google-oauth2":
            social_data ={
                "first_name" : kwargs['details']['first_name'],
                 "last_name" : kwargs['details']['last_name'],
            }
        elif backend.name == "facebook":
            social_data ={
                'first_name': kwargs['details']['first_name'],
                "last_name":  kwargs['details']['last_name'],
            }

        attrs = dict(attrs, **social_data)
        PbProfile.objects.create(
                    **attrs
        )
    else:
        # try:
            if PbUserOauthToken.objects.filter(user=user.id).exists():
                token=PbUserOauthToken.objects.get(user=user.id)
                token.linkedin = response.get("access_token")
                token.save()
            else:
                PbUserOauthToken.objects.create(
                    user=user,
                    linkedin=response.get("access_token"),
                )
        # except:
        #     pass


def associate_with_user(backend,user,response,*args,**kwargs):
    try:
        PbProfile.objects.get(user_id=user.id)
    except PbProfile.DoesNotExist:
        save_profile_from_social(backend,user,response,*args,**kwargs)