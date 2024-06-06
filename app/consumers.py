import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Transaction

class TransactionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        transaction_type = text_data.get('transaction_type')
        amount = float(text_data.get('amount'))
        member = self.scope['user'].member

        if transaction_type == 'Deposit':
            member.balance += amount
        elif transaction_type == 'Saving':
            member.balance += amount
        elif transaction_type == 'Withdrawal':
            if member.balance >= amount:
                member.balance -= amount
            else:
                await self.send(text_data='Insufficient balance')
                return

        transaction = Transaction(member=member, transaction_type=transaction_type, amount=amount)
        transaction.save()

        await self.send(text_data=f'Transaction successful. New balance: {member.balance}')