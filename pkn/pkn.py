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
from numpy import arange, exp, sqrt, ones, size, zeros, where, delete
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import matplotlib.mlab as mlab 
import plotly as py
import plotly.tools as tls
from math import pi
from scipy.optimize import fsolve
from scipy.special import erfc

# Ref. [2] Eqn. 9.41
def w_avg(L, mu, q, E_plane):
  return 2.05*(mu*q*L/E_plane)**(1/4)

# Ref. [2] Eqn. 9.42
def beta(L, t, Sp, C, mu, q, E_plane):
  w = w_avg(L, mu, q, E_plane)
  return 2*C*sqrt(pi*t)/(w+2*Sp)

# Ref. [2] Eqn. 9.42
def carter(L, t, Sp, q, C, h, mu, E_plane):
  w = w_avg(L, mu, q, E_plane)
  b = beta(L, t, Sp, C, mu, q, E_plane)
  return L - (w + 2*Sp)*q/4/C**2/pi/h*(exp(b**2)*erfc(b) + 2*b/sqrt(pi) - 1)  

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
  # material balance model: 'noleak', 'carter', 'largeleak'

  # Calculations
    
  # define plane strain modulus if not defined
  E_plane = E/(1-nu**2)

  # define shear modulus if not defined
  G = E/2/(1+nu)

  # Time required to reach specified fracture half-lengths
  t_dict = {
    # Ref. [2] Eqn. 9.13
    'noleak': (L/0.524/(q**3*E_plane/mu/h**4)**(1/5))**(5/4),
    'carter': float(fsolve(lambda t, L, Sp, q, C, h, mu, E_plane: 
              carter(L, t, Sp, q, C, h, mu, E_plane), 1, 
                      args=(L, Sp, q, C, h, mu, E_plane))),
    # Ref. [3] Eqn. 1-18
    'largeleak': (L*pi*C*h/q)**2
  }

  # calculate the time
  t = t_dict[balance]

  # fracture width at the wellbore
  ww0_dict = {
    # Ref. [2] Eqn. 9.40
    'noleak': 3.27*(q*mu*L/E_plane)**(1/4),
    'carter': 3.27*(q*mu*L/E_plane)**(1/4),
    # Ref. [3] Eqn. 1-19
    'largeleak': 4*(2*(1-nu)*mu*q**2/pi**3/G/C/h)**(1/4)*t**(1/8)
  }

  ww0 = ww0_dict[balance]

  # net pressure at the wellbore
  pnw_dict = {
    # Ref. [2] Eqn. 9.1
    'noleak': E_plane/2/h*ww0,
    'carter': E_plane/2/h*ww0,
    # Ref. [3] Eqn. 1-20
    'largeleak': 4*(2*G**3*mu*q**2/pi**3/(1-nu)**3/C/h**5)**(1/4)*t**(1/8)
  }

  pnw = pnw_dict[balance]

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

  t = arange(tstart, tend+inc, inc)

  # remove zero from the start time
  t = delete(t, where(t==0)[0])

  # material balance model: 'noleak', 'carter', 'largeleak'

  # Calculations
    
  # define plane strain modulus if not defined
  E_plane = E/(1-nu**2)

  # define shear modulus if not defined
  G = E/2/(1+nu)

  # Fracture half-lengths over time
  L = zeros(t.size)
  if (balance=='carter'):
    for i in range(t.size):
      L[i] = fsolve(carter,1,args=(t[i], Sp, q, C, h, mu, E_plane))

  else:
    L_dict = {
      # Ref. [2] Eqn. 9.13
      'noleak': (625/512/pi**3)**(1/5)*(q**3*E_plane/mu/h**4)**(1/5)*t**(4/5),
      # Ref. [2] 
      # 'carter': fsolve(carter,ones(t.size),args=(t, Sp, q, C, h, mu, E_plane)),
      # Ref. [3] Eqn. 1-18
      'largeleak': q/pi/C/h*t**(1/2)
    }

    L = L_dict[balance]

  # fracture width at the wellbore
  ww0_dict = {
    # Ref. [2] Eqn. 9.40
    'noleak': 3.27*(q*mu*L/E_plane)**(1/4),
    'carter': 3.27*(q*mu*L/E_plane)**(1/4),
    # Ref. [3] Eqn. 1-19
    'largeleak': 4*(2*(1-nu)*mu*q**2/pi**3/G/C/h)**(1/4)*t**(1/8)
  }

  ww0 = ww0_dict[balance]

  # net pressure at the wellbore
  pnw_dict = {
    # Ref. [2] Eqn. 9.1
    'noleak': E_plane/2/h*ww0,
    'carter': E_plane/2/h*ww0,
    # Ref. [3] Eqn. 1-20
    'largeleak': 4*(2*G**3*mu*q**2/pi**3/(1-nu)**3/C/h**5)**(1/4)*t**(1/8)
  }

  pnw = pnw_dict[balance]

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