# Django-Tutorial
->Django Set up
->File structure
->Creation of app
->Basic API (first api)
->Models and fields
->ORMs  -> all(),get(),create(),save(),filter(),delete(),count(),first(),last()
->Relations in model  ->One to One   
                      ->One to Many
                      ->Many to Many
->Views, APIViews
REST FRAMEWORK: (CRUD)
->POST   (c)
->GET    (r)
->PUT    (u)
->DELETE (d)

->Serializers 
        ->Basic Serializers
        ->SerializerMethodField
        ->get_attribute

->GenericAPIVIews :
        ->ListAPIView
        ->CreateAPIView
        ->UpdateAPIView
        ->DestroyAPIView

        ->ListCreateAPIView
        ->RetrieveUpdateDestroyAPIView       




Naming conventions:
Model -> _name_,Model
ex:StudentModel

Serializer -> modelname,type,serializer
                       ->List
                       ->Create
                       ->Update
ex:StudentModelListSerializer
ex:StudentModelCreateSerializer

Views -> modelname,type,APIView
ex:StudentModelListAPIView

routes -> modelname,type,api-view
ex:student-details-list-api-view/
ex:student-details-create-api-view/


Generic Views