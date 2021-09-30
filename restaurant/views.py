from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from restaurant.models import Category, Restaurant, FoodMenu, Comment


# 식당보기 > 식당 리스트가 나오는 페이지
class RestaurantListView(ListView):
    # 어떤 테이블에서 객체 리스트를 가져올 것인지 지정해주기
    model = Restaurant
    # 템플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    context_object_name = 'restaurant_list'
    # 템플릿 파일 위치 지정
    template_name = 'restaurant/category.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 현재 선택된 식당 분류
        context['category'] = Category.objects.all()
        # 선택된 식당 분류에 해당하는 식당 목록
        context['restaurant_list'] = Restaurant.objects.all()
        return context


# 식당보기 > 식당 리스트가 나오는 페이지 (선택한 카테고리별 메뉴가 나오도록)
def RestaurantList(request, id):
    category = Category.objects.all()
    restaurant = Restaurant.objects.all()
    if id:
        current_category = get_object_or_404(Category, id=id)
        restaurant = Restaurant.objects.filter(category=current_category)
    context = {'category': category, 'restaurant_list': restaurant}
    return render(request, 'restaurant/category.html', context)


# 식당 상세보기 : 식당의 기본 정보, 메뉴 목록, 후기 목록 load
class RestaurantDetailView(DetailView):
    model = Restaurant
    context_object_name = 'restaurant_detail'
    template_name = 'restaurant/restaurant.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 현재 선택된 식당
        context['restaurant'] = self.restaurant
        # 현재 선택된 식당의 메뉴 목록
        context['menu_list'] = FoodMenu.objects.filter(restaurant=self.restaurant)
        # 현재 선택된 식당에 대한 후기 목록
        context['comment_list'] = Comment.objects.filter(restaurant=self.restaurant)
        return context

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            self.restaurant = Restaurant.objects.get(pk=kwargs['pk'])
        return super().get(request, *args, **kwargs)


# 식당 후기 등록
def CreateRestaurantComment(request, id):
    if request.method == "POST":
        restaurant = get_object_or_404(Restaurant, id=id)
        review_content = request.POST.get('review_content')
        review_menu = request.POST.get('review_menu')
        menu = get_object_or_404(FoodMenu, id=review_menu)
        review_image = request.POST.get('review_image')
        Comment.objects.create(restaurant=restaurant, menu=menu, content=review_content, thumbnail=review_image)
    return redirect('restaurant:restaurant_detail', id)