#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Stock model class.
#
###############################################################################

class Stock(Mixin, db.Model):
    """
    Stock table.
    """
    __tablename = "stock"


