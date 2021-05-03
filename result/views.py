from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.forms.models import formset_factory
from django.views.generic import (
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from student.models import Student
from .models import Result
from .forms import ResultForm, ResultFormSet
from .filters import ResultFilter

def is_element_exisits(year_term, results, student):
    for elem in results[year_term]:
        if student in elem.keys():
            return True
        return

class AllRusltView(LoginRequiredMixin, FilterView):
    model = Result
    template_name = 'result/results_list.html'
    filterset_class = ResultFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        results = {}
        queryset = Result.objects.all()
        all_results = ResultFilter(self.request.GET, queryset=queryset)

        for result in all_results.qs:
            year = result.year
            term = result.term
            if f"{year}_{term}" in results.keys():
                results[f"{year}_{term}"] += [result]
            else:
                results[f"{year}_{term}"] = [result]

        context['results'] = results
        return context
        
    
class AllStudentResultDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'result/all_result_detail.html'
    context_object_name = 'student'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        results = {}
        student_results = self.object.result.all()

        for result in student_results:
            year = result.year
            term = result.term
            if f"{year}_{term}" in results.keys():
                results[f"{year}_{term}"] += [result]
            else:
                results[f"{year}_{term}"] = [result]

        context['results'] = results
        return context
        


class ResultDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'result/result_detail.html'
    context_object_name = 'student'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        year = self.kwargs['year']
        term = self.kwargs['term']
        
        final_result = self.object.result.filter(Q(year=year) & Q(term=term) )
        
        total_score = 0
        total_subjects_score = 0

        for result in final_result:
            total_score+=result.exam_score

        for result in final_result:
            total_subjects_score+=result.subject_score
        
        context['total_score'] = total_score
        context['total_subjects_score'] = total_subjects_score
        
        context['year'] = year
        context['term'] = term
        
        context['final_result'] = final_result
        
        return context
        
        
class ResultCreateView(LoginRequiredMixin, CreateView):
    model = Result
    template_name = 'result/result_form.html'
    fields = ('student', 'term', 'year')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.method == 'POST':
            result_form = ResultFormSet(self.request.POST)
            form = ResultForm(self.request.POST)
        else:
            result_form = ResultFormSet()
            form = ResultForm()
        
        context['result_form'] = result_form
        context['form'] = form
        
        return context
        
    def form_valid(self, form,**kwargs):
        context = self.get_context_data()
        
        result_form = context['result_form']
        form = context['form']
        
        if result_form.is_valid() and form.is_valid():
            new_form = form.save(commit=False)
            student = new_form.student
            term = new_form.term
            year = new_form.year
            
            result_form.instance = student
            
            results = result_form.save(commit=False)
            
            for instance in results:
                instance.term = term
                instance.year = year
                instance.save()
            
            return redirect('students_list')
        
        
class DetleteResultView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'result/result_delete_confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        self.year = self.kwargs.get('year')
        self.term = self.kwargs.get('term')

        student = self.get_object()
        
        self.results = student.result.filter( Q(year=self.year) & Q(term=self.term) )
       
       
        total_score = 0
        total_subjects_score = 0

        for result in self.results:
            total_score+=result.exam_score
            total_subjects_score+=result.subject_score
        
        context['total_score'] = total_score
        context['total_subjects_score'] = total_subjects_score
        
        context['year'] = self.year
        context['term'] = self.term
        context['results'] = self.results

        print(context)
        
        return context
        
        
    def delete(self, *args, **kwargs):
        success_url = self.get_success_url()
        
        term = self.kwargs.get('term')
        year = self.kwargs.get('year')
        
        student = self.get_object()
        
        results = student.result.filter( Q(year=year) & Q(term=term) )
        
        for result in results:
            result.delete()
            
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('student', kwargs={'pk':self.kwargs['pk']})
    
    