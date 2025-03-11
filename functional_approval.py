import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import itertools

# Part 0 ----------------------------------
# Define the ApprovalSet class (approval set)
class ApprovalSet:
    # Initialize Class
    def __init__( self, name, function ):
        self.name = name
        self.function = function
  
    def edit_set( self, newname, newfunction ):
        self.name = newname
        self.function = newfunction
    
    def find_support( self, xmin, xmax ):
        x = np.linspace(xmin, xmax, 100)
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
    def __init__( self, name, tick = 0.5 ):
        self.name = name
        self.approval_sets = [] # initialize with empty approval sets
        self.num_voters = 0
        self.tick = tick
        
        # List of all endpoints and setnames (useful when checking for left-right alternation)
        self.list_setnames = []
   
    ## DISPLAYING / OBTAINING BASIC INFORMATION ABOUT THE CIRCULAR SOCIETY----         
    # Method to print society information
    def print_society_info( self ):
        print("Circular Society Name: " + self.name)
        print("Number of Voters: " + str(self.num_voters) )
        print(f"Approval Set names: {self.list_setnames}" )
   
    ### FINDING, EDITING, ADDING, REMOVING APPROVAL SETS-----------------------
    def find_approval_set( set_name ):
        for ind, A in enumerate( self.approval_sets ):
            if set_name == A.name:
                return ind
        return -1

    # Method to add a new approval set into the society
    def add_approval_set( self, set_name, approval_function ):
        new_set = ApprovalSet( set_name, approval_function)
        # Update attributes
        self.approval_sets.append( new_set )
        self.num_voters += 1
        
        # Update list of all endpoints
        self.list_setnames.append( set_name )
               
    # Method to remove an approval set from the society
    def removeApprovalSet( self, set_name ):
        for ind, A in enumerate( self.approval_sets ):
            if set_name == A.name:
                self.approval_sets.pop(ind)
                self.list_setnames.pop(ind)
                self.num_voters -= 1
    
    # Method to edit the endpoints of an approval set
    def editApprovalSet( self, set_name, approval_function ):
        ind = self.find_approval_set( set_name ) # if not found, ind = -1
        
        if ind == -1:
            print("Set name is not found")
        else:
            A = self.approvalSets[ind]
            A.editSet( set_name, approval_function )
       
    ### VISUALIZATION --------------------------------------------------------
    
    # Method to visualize the sets
    def visualize( self, fig_path=None, xmin=0, xmax=10, ymin=0, ymax=5 ):
        
        ## Set up grid
        fig = plt.figure()
        ax = fig.add_subplot(2, 1, 1)
        # Major ticks every 1, minor ticks every self.tick (default = 0.5)
        major_ticks = np.arange(xmin, xmax, self.tick * 2)
        minor_ticks = np.arange(xmin, xmax, self.tick)        
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        #ax.set_yticks(major_ticks)
        #ax.set_yticks(minor_ticks, minor=True)
        # Different thickness settings for the major and minor grids:
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        plt.yticks(np.arange(0, self.num_voters+1, step = 1) )

        # colormap
        colors = plt.cm.jet(np.linspace(0, 1, self.num_voters) )
        
        # Draw the functions
        for ind, A in enumerate( self.approval_sets ):
            left_endpt, right_endpt = A.find_support(xmin, xmax)
            x = np.linspace(left_endpt, right_endpt, 10)
            y = [A.function(pt) for pt in x]
            plt.plot( x, y, color=colors[ind], label=A.name)
            plt.plot( left_endpt, A.function(left_endpt), color=colors[ind], marker="o" )
            plt.plot( right_endpt, A.function(right_endpt), color=colors[ind], marker="o" )

        ax.set_ylim(ymin, ymax)
        ax.legend(bbox_to_anchor = [1, 1], loc = 'center left' )
        if fig_path:
            plt.savefig(fig_path)


    def plot_count_function( self, fig_path=None, xmin=0, xmax=10, ymin=0, ymax=5 ):
        
        ## Set up grid
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        # Major ticks every 1, minor ticks every self.tick (default = 0.5)
        major_ticks = np.arange(xmin, xmax, self.tick * 2)
        minor_ticks = np.arange(xmin, xmax, self.tick)        
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        #ax.set_yticks(major_ticks)
        #ax.set_yticks(minor_ticks, minor=True)
        # Different thickness settings for the major and minor grids:
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        plt.yticks(np.arange(0, self.num_voters+1, step = 1) )

        X = np.linspace(xmin, xmax, 1000)
        Y = np.array([0 for pt in X])

        # Draw the functions
        for ind, A in enumerate( self.approval_sets ): 
            Y = Y + [A.function(pt) for pt in X]

        plt.plot( X, Y)
        ax.set_ylim(ymin, ymax)
        
        if fig_path:
            plt.savefig(fig_path)


