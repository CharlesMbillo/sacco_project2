from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def transaction(request):
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        amount = float(request.POST.get('amount'))
        member = request.user.member

        if transaction_type == 'Deposit':
            member.balance += amount
        elif transaction_type == 'Saving':
            member.balance += amount
        elif transaction_type == 'Withdrawal':
            if member.balance >= amount:
                member.balance -= amount
            else:
                return redirect('index')

        transaction = Transaction(member=member, transaction_type=transaction_type, amount=amount)
        transaction.save()

        return redirect('transaction')

    return render(request, 'transaction.html')

class TransactionList(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)