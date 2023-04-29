from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products.count()

        '''
        the view checks if the category_slug parameter is not None. 
        If it is not None, the view uses the get_object_or_404 shortcut function 
        to retrieve a Category object from the database 
        with the matching slug attribute. 
        If no matching Category object is found, 
        a 404 error is raised.
        '''
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
    # Explain the return render
    # => The reason why only these three arguments are passed to render is
    '''
    because they are the minimum required arguments to render a template. 
    The request argument is required because it contains information about 
    the user's request, such as the HTTP method used and any submitted form data. 
    The template file name is required to know which template to render. 
    The context argument is required to pass data to the template for rendering.
    '''


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product
    }
    return render(request, 'store/product_detail.html', context)

# 위의 코드는 Django 앱에서 상품 세부 정보 페이지를 렌더링하는 데 사용됩니다.
# product_detail 함수는 HTTP 요청(request 객체)과 category_slug, product_slug 두 개의 URL 매개변수를 받습니다.
# 이 함수는 Product 모델에서 해당 카테고리와 제품 슬러그에 해당하는 단일 제품을 검색합니다.
# try-except 블록은 Product 인스턴스를 검색하면서 발생할 수 있는 예외를 처리합니다.
# 예외가 발생하면 except 블록이 실행되고, raise e 문을 사용하여 예외를 다시 발생시킵니다.
# 이를 통해 예외가 발생한 이유에 대한 정보를 출력하고 디버깅을 수행할 수 있습니다.

# context 변수는 single_product을 포함하는 딕셔너리입니다.
# 이 변수는 render 함수에 전달되어 템플릿에서 사용할 수 있도록 합니다.
# render 함수는 product_detail.html 템플릿을 렌더링하고,
# context 변수에 저장된 데이터를 템플릿에 전달합니다.

# 최종적으로 render 함수는 렌더링된 HTML을 포함하는 HTTP 응답 객체를 반환합니다.
# 이 응답 객체는 웹 브라우저에게 반환되어 상품 세부 정보 페이지를 표시합니다.
