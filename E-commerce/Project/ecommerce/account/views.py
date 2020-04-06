from django.shortcuts import render

# Create your views here.
class Signup(APIView):

    def post(self,request):
        
        response_dict = {"status": True, "message": "", "data": {}}
        try:
            username=request.data.get('username')
            email=request.data.get('email')
            password=request.data.get('password')
            phone = request.data.get('phone')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        ud = UserDetail(user=user,phone=phone,created_by=request.user.id)
        ud.save()
        response_dict = {"status": True, "msg":"Successfully Registered"}
        return Response(response_dict)
            
    except Exception as e:
        response_dict = {"status": False}
        return Response(response_dict)