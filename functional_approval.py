import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import itertools

# Part 0 ----------------------------------
# Define the ApprovalSet class (approval set)
class ApprovalSet:
    # Initialize Class
    def __init__( self, name, function, xmin=0, xmax=10 ):
        self.name = name
        self.function = function
        self.left_endpt, self.right_endpt = self.find_support(xmin=xmin, xmax=xmax)

    def edit_set( self, newname, newfunction ):
        self.name = newname
        self.function = newfunction

    def find_support( self, xmin=0, xmax=10, prec=0.001 ):
        x = np.arange(xmin, xmax+prec, prec)
        index_nonzero = [ i for i, pt in enumerate(x) if self.function(pt) > 0 ]
        left_endpt = x[min(index_nonzero)]
        right_endpt = x[max(index_nonzero)]
        return left_endpt, right_endpt

    def is_point_in_support( self, point):
        check = self.function(point) > 0

        return check

# Part 1 - MAIN ----------------------------------

# Define the Society class

class Society:

    # Initialize Class
    def __init__( self, name=None, prec=0.001 ):
        self.name = name
        self.approval_sets = dict() # initialize with an empty collection of approval sets
        self.num_voters = 0

        # List of endpoint information
        self.xmin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None

        # Precision used for plotting
        self.prec = prec

        # Count functions
        self.X = None
        self.count_function = None
        self.binary_count_function = None

    ## DISPLAYING / OBTAINING BASIC INFORMATION ABOUT THE CIRCULAR SOCIETY----
    # Method to print society information
    def print_society_info( self ):
        print(f"Society Name: {self.name}")
        print(f"Number of Voters: {self.num_voters}" )
        print(f"Approval Set names: {self.approval_sets.keys()}" )
        print(f"xmin: {self.xmin}, xmax={self.xmax}, ymin={self.ymin}, ymax={self.ymax}")

    ### FINDING, EDITING, ADDING, REMOVING APPROVAL SETS-----------------------
    def get_approval_set( self, set_name ):
        if set_name in self.approval_sets.keys():
            return self.approval_sets[set_name]
        else:
            return None

    def update_spectrum( self ):
        if len(self.approval_sets) == 0:
            self.xmin = None
            self.xmax = None
            self.ymin = None
            self.ymax = None
        else:
            self.xmin = np.min( np.array([A.left_endpt for A in self.approval_sets.values()]) )
            self.xmax = np.max( np.array([A.right_endpt for A in self.approval_sets.values()]) )
            Y = np.array([ 
                A.function(pt) for A in self.approval_sets.values()
                for pt in np.arange(A.left_endpt, A.right_endpt+self.prec, self.prec)
           ])
            self.ymin = min(0, np.min(Y))
            self.ymax = np.max(Y)

    def update_count_functions( self ):
        if len(self.approval_sets) == 0:
            self.X = None
            self.count_function = None
        else:
            self.X = np.arange(self.xmin, self.xmax + self.prec, self.prec)
            Y1 = np.zeros_like(self.X)
            Y2 = np.zeros_like(self.X)
            for A in self.approval_sets.values():
                Y1 = Y1 + np.array([ A.function(pt) for pt in self.X])
                Y2 = Y2 + np.array([ 1 if A.function(pt)>0 else 0 for pt in self.X])
            self.count_function = Y1
            self.binary_count_function = Y2

    def add_approval_set( self, set_name, approval_function ):
        new_set = ApprovalSet( set_name, approval_function)
        # Update attributes
        self.approval_sets[set_name] = new_set
        self.num_voters += 1
        self.update_spectrum()
        self.update_count_functions()

    def remove_approval_set( self, set_name ):
        self.approval_sets.pop(set_name)
        self.num_voters -= 1
        self.update_spectrum()
        self.update_count_functions()

    def edit_approval_set( self, set_name, approval_function ):
        A = self.get_approval_set( set_name ) # if not found, A is None
        if A is None:
            print("Set name is not found")
        else:
            A.edit_set( set_name, approval_function )
        self.update_spectrum()
        self.update_count_function()


    ### VISUALIZATION --------------------------------------------------------
    def setup_grid( self, ax, xmin, xmax, ymin, ymax, prec, tick ):
        major_ticks = np.arange(xmin, xmax+prec, 1)
        minor_ticks = np.arange(xmin, xmax+prec, tick)
       # Set up grid
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        # Different thickness settings for the major and minor grids:
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        ax.set_ylim(ymin, ymax+0.5)
        ax.set_yticks(np.arange(ymin, ymax+prec, 1))
        ax.set_yticks(np.arange(ymin, ymax, 0.5), minor=True)

    def plot_summary_function( self, ax, X, Y, label, tick=1/3):
        max_Y = np.max(Y)
        argmax_Y = [ x for x, y in zip(X, Y) if y==max_Y]
        ymax = max(self.ymax, max_Y+1)

        ax.plot( X, Y , label=label )
        ax.set_title( label )
        ax.axvline(
            x=argmax_Y[0], ymin=self.ymin, ymax=ymax,
            linestyle='--', color='red', linewidth=0.5
        )
        if len(argmax_Y) > 1:
            ax.axvline(
                x=argmax_Y[-1], ymin=self.ymin, ymax=ymax,
                linestyle='--', color='red', linewidth=0.5
            )
        ax.axhline(
            y=max_Y, xmin=self.xmin, xmax=self.xmax,
            linestyle='--', color='red', linewidth=0.5
        )
        ax.text(x = 0, y = max_Y, s=str(round(max_Y, 2)), color='red')
        ax.legend(bbox_to_anchor = [1, 1], loc = 'upper left' )
        self.setup_grid(ax, self.xmin, self.xmax, self.ymin, ymax, self.prec, tick )


    # Method to visualize the sets, count function, and approval count
    def visualize(
            self,
            plot_approval_sets = True ,
            plot_count_function = True,
            plot_binary_count = True,
            plot_combination_count = True,
            c = 0.5, 
            fig_path=None,
            xmin=None, xmax=None, ymin=None, ymax=None,
            tick=1/3, prec=None      
        ):

        if xmin is None:
            xmin = self.xmin
        if xmax is None:
            xmax = self.xmax
        if ymin is None:
            ymin = self.ymin
        if ymax is None:
            ymax = self.ymax
        if prec is not None:
            self.prec = prec

        ## Plot Setup
        nrows = int(plot_approval_sets)+int(plot_count_function) + int(plot_binary_count) + int(plot_combination_count)
        fig, axs = plt.subplots(nrows = nrows, ncols = 1, sharex=True)
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.75)

        r = 0
        if plot_approval_sets:
            # Draw the functions
            colors = plt.cm.jet(np.linspace(0, 1, self.num_voters) )
            for ind, A in enumerate(self.approval_sets.values()):
                x = np.arange(A.left_endpt, A.right_endpt+self.prec, self.prec )
                y = [A.function(pt) for pt in x]
                axs[r].plot( x, y, color=colors[ind], label=A.name)
                axs[r].plot( A.left_endpt, A.function(A.left_endpt), color=colors[ind], marker="o" )
                axs[r].plot( A.right_endpt, A.function(A.right_endpt), color=colors[ind], marker="o" )
            axs[r].legend(bbox_to_anchor = [1, 0], loc = 'lower left' )
            axs[r].set_title('Approval Functions')
            self.setup_grid(axs[r], xmin, xmax, ymin, ymax, self.prec, tick)
            r =+ 1

        if plot_count_function:
            self.plot_summary_function( axs[r], self.X, self.count_function, label='Count Function', tick=tick)
            r += 1

        if plot_binary_count:
            self.plot_summary_function( axs[r], self.X, self.binary_count_function, label='Binary Count Function', tick=tick)
            r += 1
        if plot_combination_count:
            self.plot_summary_function( 
                axs[r], self.X, c * self.count_function+ (1-c) * self.binary_count_function, 
                    label=f'{c}*Count+{1-c}*Binary Count', tick=tick
            )

        if fig_path:
            plt.savefig(fig_path)

    # Method to check (k, m) agreeability (brute force)
    def check_agreeability( self, k, m):
        set_names = [ A.name for A in self.approval_sets.values() ]

        # get all subsets of size m
        subcollections_m = [list(i) for i in itertools.combinations(set_names, m)]
        good_m_set_indicator = [] # is the society k,m agreeable? will store 1 or 0 for each collection of m sets
        bad_m_sets = []

        # go through each subset of size m
        for collection in subcollections_m:

            xmin = 0
            xmax = 10
            X = np.arange(self.xmin, self.xmax + self.prec, self.prec)
            Y = np.zeros_like(X)

            # Compute count function
            for set_name in collection:
                A = self.get_approval_set(set_name)
                Y = Y + np.array([A.function(pt) for pt in X])
            if np.max(Y) >= k:
                good_m_set_indicator.append(1)
            else:
                good_m_set_indicator.append(0)
                bad_m_sets.append(collection)

        good_m_set_indicator = np.array(good_m_set_indicator)
        is_km_agreeable = np.prod(good_m_set_indicator) == 1

        return is_km_agreeable, bad_m_sets
