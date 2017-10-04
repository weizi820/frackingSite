# PKN
#   ----------------------------------------------------------------------
#   Created by Endrina Rivas
#       endrina.rivas@uwaterloo.ca
#       Department of Civil Engineering
#       University of Waterloo
#       September 2017
#   Last Updated September 2017
#   References: 
#       [1] Nordgren, R. P. (1972). Propagation of a Vertical Hydraulic 
#           Fracture. Society of Petroleum Engineers Journal, 12(4),
#       [2] Valko, P., & Economides, M. J. (1995). Hydraulic Fracture Mechanics. 
#           New York: John Wiley & Sons.
#       [3] Yew, C. H. (1997). Mechanics of hydraulic fracturing. 
#           Houston, Tex: Gulf Pub. Co.
#   ----------------------------------------------------------------------
import numpy as np 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import matplotlib.mlab as mlab 
import plotly as py
import plotly.tools as tls
import math 

def pkn_plot_design(L, h, q, E, nu, mu, C, Sp, balance):
  # Model Input 
  # E: Young's modulus
  # nu: Poisson's ratio
  # fluid-loss coefficient
  # spurt loss coefficient
  # fracture height
  # fluid viscosity
  # fluid injection flow rate
  # simulation time
  # material balance model: 'no-leak', 'carter', 'large-leak'

  # Calculations
    
  # define plane strain modulus if not defined
  try: 
    E_plane
  except NameError:
    E_plane = E/(1-nu**2)

  # define shear modulus if not defined
  try:
    G 
  except NameError:
    G = E/2/(1+nu)

  # Time required to reach specified fracture half-lengths
  try: 
    t_dict = {
      # Ref. [2] Eqn. 9.13
      'no-leak': (L/0.524/(q**3*E_plane/mu/h**4)**(1/5))**(5/4),
      'carter': 0,
      # Ref. [3] Eqn. 1-18
      'large-leak': (L*math.pi*C*h/q)**2
    }
  except: 
    t_dict = {}

  # calculate the time
  t = t_dict[balance]

  # fracture width at the wellbore; Ref. [3] Eqn. 1-22
  ww0 = 3.27*(q*mu*L/E_plane)**(1/4)

  # net pressure at the wellbore; Ref. [3] Eqn. 1-23
  pnw = E_plane/2/h*ww0

  # Post-processing
  # TODO: add some figures!

  return t, ww0, pnw

def pkn_plot_analysis(tstart, tend, inc, h, q, E, nu, mu, C, Sp, balance):
  # Model Input 

  # E: Young's modulus
  # nu: Poisson's ratio
  # fluid-loss coefficient
  # spurt loss coefficient
  # fracture height
  # fluid viscosity
  # fluid injection flow rate
  # simulation time
  t = np.arange(tstart, tend, inc)

  # material balance model: 'no-leak', 'carter', 'large-leak'

  # Calculations
    
  # define plane strain modulus if not defined
  try: 
    E_plane
  except NameError:
    E_plane = E/(1-nu**2)

  # define shear modulus if not defined
  try:
    G 
  except NameError:
    G = E/2/(1+nu)

  # Fracture half-lengths over time
  try:
    L_dict = {
      # Ref. [2] Eqn. 9.13
      'no-leak': (625/512/math.pi**3)**(1/5)*(q**3*E_plane/mu/h**4)**(1/5)*t**(4/5),
      'carter': 0,
      # Ref. [3] Eqn. 1-18
      'large-leak': q/math.pi/C/h*t**(1/2)
    }
  except:
    L_dict = {}

  L = L_dict[balance]

  # fracture width at the wellbore; Ref. [3] Eqn. 1-22
  ww0 = 3.27*(q*mu*L/E_plane)**(1/4)

  # net pressure at the wellbore; Ref. [3] Eqn. 1-23
  pnw = E_plane/2/h*ww0

  # Post-processing

  fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(450/50, 450/50), dpi=50)

  line1, = ax0.plot(t, L)
  ax0.set_title('Half-length vs. time')

  line2, = ax1.plot(t, ww0)
  ax1.set_title('Fracture width at wellbore over time')

  line3, = ax2.plot(t, pnw)
  ax2.set_title('Net pressure at wellbore over time')

  line4, = ax3.plot(ww0, L)
  ax3.set_title('Fracture width at wellbore over fracture length')

  # fig.tight_layout()

  plotly_fig = tls.mpl_to_plotly( fig )
  plot_url = py.offline.plot( plotly_fig, auto_open=False, show_link=False, filename='pkn/templates/pkn/pkn_plot.html')

  return plot_url