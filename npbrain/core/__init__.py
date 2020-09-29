# -*- coding: utf-8 -*-

"""
This module defines the core of the framework, including the
abstraction of ``Neurons``, ``Synapses``, ``Monitor``, ``Network``,
and numerical integration methods.

The core is so small, and the overall framework is easy to
understand. Using it, you can easily write your own neurons,
synapses, etc.
"""


from npbrain.core.network import *
from npbrain.core.neuron_group import *
from npbrain.core.synapse_connection import *
from npbrain.core.integrator import *


