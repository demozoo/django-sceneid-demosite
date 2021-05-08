from sceneid.apps import SceneIDConfig

class DemositeSceneIDConfig(SceneIDConfig):
    connect_template_name = 'accounts/connect.html'
    connect_register_form_class = 'accounts.forms.SceneIDUserCreationForm'
