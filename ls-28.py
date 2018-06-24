#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docx

document = docx.Document()
document.add_paragraph('Hello,Word!')
document.save('demo.docx')