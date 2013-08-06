#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : OKF - Spending Stories
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 06-Aug-2013
# Last mod : 06-Aug-2013
# -----------------------------------------------------------------------------
from webapp.core.models import Story, Theme
from webapp.currency.models import Currency
from rest_framework import viewsets
import serializers

class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows story to be viewed or edited.
    """
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer

class ThemeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Theme to be viewed or edited.
    """
    queryset = Theme.objects.all()
    serializer_class = serializers.ThemeSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Currency to be viewed or edited.
    """
    queryset = Currency.objects.all()
    serializer_class = serializers.CurrencySerializer

# EOF
