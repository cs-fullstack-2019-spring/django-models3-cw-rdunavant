from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Test URL")

def newBook(request):
    newBook = Book(name = "Dogland", pageNumber= "350", genre="fiction", publishDate="12/03/03")
    return HttpResponse(newBook)

def all(request):
    allNames=""
    allEntries=Book.objects.all()
    for eachElement in allEntries:
        allNames +=eachElement.name + "<br>"
        return HttpResponse(allNames)
def  greaterThanOrEqualTo01012018(request):
    onlyObjectsGreaterThanOrEqualTo01012018=Book.objects.filter(age__gt==01012018)
    return HttpResponse(onlyObjectsGreaterThanOrEqualTo01012018)

def newCar(request):
    newCar = Car(make = "Ford", model = "Expedition", year="2009")
    return HttpResponse(newCar)

def all(request):
    allYears=""
    allEntries=Car.objects.all()
    for eachElement in allEntries:
        allYears +eachElement.year + "<br>"
        return HttpResponse(allYears)
def greaterThan2010(request):
    onlyObjectsGreaterThan2010=Car=objects.filter(year__gt 2010)
    return HttpResponse(onlyObjectsGreaterThan2010)