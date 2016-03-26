from django.shortcuts import render,HttpResponse,redirect
from django.http import Http404
from recipes.models import Recipe
from recipes.forms import RecipeForm

# Create your views here.

def recipe_list(request):

    recipelist=Recipe.objects.all()

    context = {'recipelist':recipelist}

    return render(request,'recipelist.html',context)

def recipe(request, recipe_id):
    try:
        recipe=Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404
    context = {'recipe':recipe}
    return render (request, 'recipe.html',context)

def addrecipe(request):
    """Create a form that can be used to add a new recipe.
    Save data submitted through the form to the database as a new recipe.
    """

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            r = Recipe()
            r.name = data['name']
            r.servings = data['servings']
            r.description = data['description']
            r.ingredients = data['ingredients']
            r.instructions = data['instructions']
            r.save()
            return redirect(recipe_list)
    else:
        form = RecipeForm()
    return render(request, 'addrecipe.html', {'form': form})
