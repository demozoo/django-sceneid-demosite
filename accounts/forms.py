from sceneid.forms import UserCreationForm as BaseUserCreationForm


class SceneIDUserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name')
