'''
   Methods for the Legal Resource Registry
'''
from traveler import Traveler
from nodes import *
from directives import *
from writer import HTMLTranslatorForLegalResourceRegistry
from transforms import MoveTrans

def role_trans(name, rawtext, text, lineno, inliner,
            options={}, content=[]):
    newnode = trans(rawsource=rawtext, text=text)
    pending = nodes.pending(MoveTrans)
    inliner.document.document.note_pending(pending)
    newnode += pending
    newnode.setup_child(pending)
    return [newnode], []

