import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from alerts.models import Alert

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user(db):
    return User.objects.create(username='testuser', password='testpassword')

@pytest.fixture
def alert(db,user):
    return Alert.objects.create(
        name='Test Alert',
        low_amount=100.0,
        high_amount=200.0,
        percentage_change=5.0,
        user=user,
    )

@pytest.mark.django_db
def test_create_alert(client, user):
    url = reverse('create_alert')
    data = {
        'name': 'New Alert',
        'low_amount': 50.0,
        'high_amount': 100.0,
        'percentage_change': 2.0,
        'user': user.id 
    }
    client.force_login(user)
    response = client.post(url, data)
    print(response.content)
    assert response.status_code == 201
    assert Alert.objects.filter(name='New Alert', user=user).exists()