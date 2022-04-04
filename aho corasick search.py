
# coding: utf-8

# In[1]:


#aho corasick is a string search algorithm for multiple patterns
#its ability to match patterns in parallel is incredible
#kmp is merely a special case of ac
#ac is the most complicated string search algorithm in this repository
#check the link below for a more detailed tutorial
# https://blogs.asarkar.com/assets/docs/algorithms-curated/Aho-Corasick%20Automata%20-%20Stanford.pdf


# In[2]:


#naïve search iterates the letter one by one
def naive_search(pattern,rawtext):
    
    len_pattern=len(pattern)
    len_rawtext=len(rawtext)
    output=[]    
    
    #this part is stupid
    #as python allows us to do 
    #rawtext[i:i+len_pattern]==pattern
    for i in range(len_rawtext-len_pattern+1):
        ignore=False
        j=0
        while not ignore:
            if rawtext[i+j]!=pattern[j]:
                ignore=True
            j+=1
            
            if j==len_pattern:
                if not ignore:
                    output.append(i)
                ignore=True
                
                
    return output


# In[3]:


#brute force search through each pattern
def naive_multi_search(patterns,rawtext):    
    arr=[naive_search(pattern,rawtext) for pattern in patterns]
    result=dict(zip(patterns,arr))    
    return result


# In[4]:


#build a trie structure where edge represents each letter
#check the link below for explanation on suffix tree
# https://www.cs.jhu.edu/~langmea/resources/lecture_notes/tries_and_suffix_tries.pdf
def build_trie(patterns):

    #initialize
    trie={0:{}}
    vertex_counter=0
    ending_vertices={}
    for pattern in patterns:
        current_vertex=0
        for letter in pattern:

            #no need to create a new branch
            #if the next letter exists in children nodes
            #move the current_vertex
            if letter in trie[current_vertex].values():
                edges=list(trie[current_vertex].values())
                current_vertex=list(trie[current_vertex].keys())[edges.index(letter)]

            #increment the vertex_counter to create a new branch
            #if the next letter does not exist in children nodes
            #move the current_vertex to vertex_counter
            else:
                vertex_counter+=1
                trie[current_vertex][vertex_counter]=letter
                trie[vertex_counter]={}
                current_vertex=vertex_counter

        #the last current_vertex marks the end of a pattern
        ending_vertices[current_vertex]=pattern
        
    return trie,ending_vertices


# In[5]:


#bfs style traversal to build suffix links and output links
#details of bfs can be found in the link below
# https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb
def build_links(trie,ending_vertices):

    #initialize
    #suffix link of root goes back to itself
    #suffix links of first layer nodes go to root
    suffix_links={0:0}
    for i in trie[0]:
        suffix_links[i]=0

    #initialize
    #all output links go nowhere
    output_links=dict(zip(range(len(trie)),[None]*len(trie)))

    #bfs style to create suffix links and output links
    #queue1 and visited1 correspond to node w in stanford material
    queue1=list(trie[0].keys())
    visited1=[]
    while queue1:

        #node w in stanford material
        parent=queue1.pop(0)
        visited1.append(parent)

        #node wa in stanford material
        for child in trie[parent]:

            #queue2 and visited2 correspond to node xyz in stanford material
            queue2=[suffix_links[parent]]
            visited2=[]
            stop=False
            while not stop:

                #node xyz
                aunt=queue2.pop(0)
                visited2.append(aunt)

                #if xa exists,the suffix link of node wa goes to xa
                if trie[parent][child] in trie[aunt].values():
                    ind=list(trie[aunt].values()).index(trie[parent][child])
                    suffix_links[child]=list(trie[aunt].keys())[ind]

                    #node u which is equivalent to node wa
                    #node v which is equivalent to node xa
                    #if node u is a pattern,output link of node v goes to node u
                    if list(trie[aunt].keys())[ind] in ending_vertices:
                        output_links[child]=list(trie[aunt].keys())[ind]

                    #if node u is not a pattern
                    #output link of node v goes to output link of node u
                    #it can either be initial value null
                    #or existing pattern via output link
                    else:
                        output_links[child]=output_links[list(trie[aunt].keys())[ind]]

                    #stop the loop
                    stop=True

                #if xa doesnt exist,follow suffix link of node x to find node yz
                else:
                    if aunt in suffix_links:
                        if suffix_links[aunt] not in queue2 and suffix_links[aunt] not in visited2:
                            queue2+=[suffix_links[aunt]]

                #stop the loop
                if len(queue2)==0:
                    stop=True

            #if no suffix link has been found
            #suffix link goes back to the root
            if child not in suffix_links:
                suffix_links[child]=0

            #bfs
            if child not in visited1:
                queue1.append(child)
                
    return suffix_links,output_links


# In[6]:


#matching process of aho corasick
def aho_corasick(patterns,rawtext):

    #reprocess
    trie,ending_vertices=build_trie(patterns)
    suffix_links,output_links=build_links(trie,ending_vertices)

    #initialize result
    result={}
    for i in patterns:
        result[i]=[]

    #start from root
    start=0

    #iterate character by character
    for i in range(len(rawtext)):
        character=rawtext[i]   

        #while current letter cannot support the traversal
        if character not in trie[start].values():
            stop=False
            while not stop:
                start=suffix_links[start]

                #if start is at the root,break the loop
                #the next letter will start at the root as well
                if start==0:
                    stop=True

                #if we can find the current letter via suffix link
                #indicating the prefix of a pattern has been validated
                #we will move start pointer to that pattern accordingly
                if character in trie[start].values():
                    stop=True
                    ind=list(trie[start].values()).index(character)
                    start=list(trie[start].keys())[ind]

        #if current letter supports the traversal
        #move start pointer further down the trie
        else:        
            ind=list(trie[start].values()).index(character)
            start=list(trie[start].keys())[ind]        

        #if there exists an output link at the start pointer
        #the existing pattern is at the start pointer
        #minus the pattern length plus one
        if output_links[start]:
            result[ending_vertices[output_links[start]]].append(
                i-len(ending_vertices[output_links[start]])+1)
            
            #trace every output along the chain of output links
            stop=False
            exhausted=output_links[start]
            while not stop:
                if output_links[exhausted]:
                    result[ending_vertices[output_links[exhausted]]].append(
                i-len(ending_vertices[output_links[exhausted]])+1)
                    exhausted=output_links[exhausted]
                else:
                    stop=True

        #if there exists a pattern at the start pointer
        #the existing pattern is at the start pointer
        #minus the pattern length plus one
        if start in ending_vertices:
            result[ending_vertices[start]].append(i-len(ending_vertices[start])+1)
            
    return result


# In[7]:


patterns=['viscosity',
 'laminar',
 'linear',
 'in',
 'line',
 'nonlinearity',
 'newton',
 'eulerian',
 'viscous',
 'newtonian']

#sort patterns by their length in ascending order
#easier to find suffix link
patterns=sorted(patterns,key=lambda x:len(x),reverse=False)


# In[8]:


#ns equation
rawtext="""In physics, the Navier–Stokes equations /nævˈjeɪ stoʊks/, named after Claude-Louis Navier and George Gabriel Stokes, describe the motion of viscous fluid substances. These balance equations arise from applying Newton's second law to fluid motion, together with the assumption that the stress in the fluid is the sum of a diffusing viscous term (proportional to the gradient of velocity) and a pressure term—hence describing viscous flow. The main difference between them and the simpler Euler equations for inviscid flow is that Navier–Stokes equations also in the Froude limit (no external field) are not conservation equations, but rather a dissipative system, in the sense that they cannot be put into the quasilinear homogeneous form:

 \\mathbf y_t + \\mathbf A(\\mathbf y) \\mathbf y_x = 0 
Navier–Stokes equations are useful because they describe the physics of many things of scientific and engineering interest. They may be used to model the weather, ocean currents, water flow in a pipe and air flow around a wing. The Navier–Stokes equations in their full and simplified forms help with the design of aircraft and cars, the study of blood flow, the design of power stations, the analysis of pollution, and many other things. Coupled with Maxwell's equations they can be used to model and study magnetohydrodynamics.

The Navier–Stokes equations are also of great interest in a purely mathematical sense. Somewhat surprisingly, given their wide range of practical uses, it has not yet been proven that in three dimensions solutions always exist, or that if they do exist, then they are smooth, i.e. they do not contain any singularity. These are called the Navier–Stokes existence and smoothness problems. The Clay Mathematics Institute has called this one of the seven most important open problems in mathematics and has offered a US$1,000,000 prize for a solution or a counter-example.[1]

Contents
1	Flow velocity
2	General continuum equations
2.1	Convective acceleration
3	Incompressible flow
3.1	Discrete velocity
3.2	Pressure recovery
4	Compressible flow
5	Other equations
5.1	Continuity equation
6	Stream function for 2D equations
7	Properties
7.1	Nonlinearity
7.2	Turbulence
7.3	Applicability
8	Application to specific problems
9	Exact solutions of the Navier–Stokes equations
9.1	A three-dimensional steady-state vortex solution
10	Wyld diagrams
11	Representations
12	Navier–Stokes equations use in games
13	See also
14	Notes
15	References
16	External links
Flow velocity
The solution of the Navier–Stokes equations is a flow velocity. It is a field, since it is defined at every point in a region of space and an interval of time. Once the velocity field is calculated, other quantities of interest, such as pressure or temperature, may be found. This is different from what one normally sees in classical mechanics, where solutions are typically trajectories of position of a particle or deflection of a continuum. Studying velocity instead of position makes more sense for a fluid; however for visualization purposes one can compute various trajectories.

General continuum equations
Main article: Derivation of the Navier–Stokes equations
See also: Cauchy momentum equation § Conservation form
The Navier–Stokes momentum equation can be derived as a particular form of the Cauchy momentum equation. In an inertial frame of reference, the conservation form of the equations of continuum[disambiguation needed] motion is:[2]

Cauchy momentum equation (conservation form)

\\frac {\\partial}{\\partial t} (\\rho \\bold u) + \\nabla \\cdot (\\rho \\bold u \\otimes \\bold u + p \\bold I)  =  \\nabla \\cdot \\boldsymbol \\tau + \\rho \\bold g

where

\\rho is the density,
\\mathbf{u} is the flow velocity,
\\nabla is the del operator.
p is the pressure
\\mathbf{I} is the identity matrix
\\boldsymbol \\tau is the deviatoric stress tensor, which has order two,
\\mathbf{g} represents body accelerations (per unit mass) acting on the continuum, for example gravity, inertial accelerations, electric field acceleration, and so on.
The left side of the equation describes acceleration, and may be composed of time-dependent, convective, and hydrostatic effects (also the effects of non-inertial coordinates if present). The right side of the equation is in effect a summation of body forces (such as gravity) and divergence of deviatoric stress.

In the Eulerian forms it is apparent that the assumption of no deviatoric stress brings Cauchy equations to the Euler equations. All non-relativistic balance equations, such as the Navier–Stokes equations, can be derived by beginning with the Cauchy equations and specifying the stress tensor through a constitutive relation. By expressing the shear tensor in terms of viscosity and fluid velocity, and assuming constant density and viscosity, the Cauchy equations will lead to the Navier–Stokes equations.

The incompressible case is simpler than the compressible one so for didactical purpose it should be presented before. However, the compressible case is the most general framework of Navier–Stokes equations so where not specified, Navier–Stokes equations are intended to be compressible Navier–Stokes equations.

Convective acceleration
See also: Cauchy momentum equation § Convective acceleration

An example of convection. Though the flow may be steady (time-independent), the fluid decelerates as it moves down the diverging duct (assuming incompressible or subsonic compressible flow), hence there is an acceleration happening over position.
A significant feature of Cauchy equation and consequently all other continuum equations (including Euler and Navier–Stokes) is the presence of convective acceleration: the effect of time-independent acceleration of a flow with respect to space. While individual fluid particles indeed experience time-dependent acceleration, the convective acceleration of the flow field is a spatial effect, one example being fluid speeding up in a nozzle.

Incompressible flow
The incompressible momentum Navier–Stokes equation result from the following assumptions on the Cauchy stress tensor:[3]

the stress is Galileian invariant: it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient \\nabla\\mathbf{u}.
the fluid is assumed to be isotropic, as with gases and simple liquids, and consequently \\mathbf  V is an isotropic tensor; furthermore, since the deviatoric stress tensor can be expressed in terms of the dynamic viscosity μ:
Stokes's stress constitutive equation (expression used for incompressible elastic solids)
\\boldsymbol \\tau = 2 \\mu \\boldsymbol \\varepsilon
where I is the identity tensor, and
\\boldsymbol{\\epsilon} := \\frac{1}{2} \\left( \\mathbf{\\nabla u} + \\mathbf{\\nabla u}^\\mathrm{T} \\right)
is the rate-of-strain tensor. So this decomposition can be explicited as:[3]
Stokes's stress constitutive equation (expression used for incompressible viscous fluids)
\\boldsymbol \\tau = \\mu (\\nabla\\mathbf{u} +  ( \\nabla\\mathbf{u} )^\\mathrm{T})
Dynamic viscosity μ need not be constant – in incompressible flows it can depend on density and on pressure. Any equation expliciting one of these transport coefficient in the conservative variables is called an equation of state.[4]

The divergence of the deviatoric stress is given by:

\\nabla \\cdot \\boldsymbol \\tau = \\mu \\nabla \\cdot  (2 \\varepsilon) = \\mu \\nabla \\cdot ( \\nabla\\mathbf{u} +  ( \\nabla\\mathbf{u} )^\\mathrm{T} ) = \\mu \\nabla^2 \\mathbf{u}
Incompressibility rules out density and pressure waves like sound or shock waves, so this simplification is not useful if these phenomena are of interest. The incompressible flow assumption typically holds well with all fluids at low Mach numbers (say up to about Mach 0.3), such as for modelling air winds at normal temperatures.[5] For incompressible (uniform density ρ0) flows the following identity holds:

\\frac 1 {\\rho_0} \\nabla p = \\nabla \\left(\\frac p {\\rho_0} \\right) \\equiv \\nabla w
where w is the specific (with the sense of per unit mass) thermodynamic work, the internal source term. Then the incompressible Navier–Stokes equations are best visualised by dividing for the density:

Incompressible Navier–Stokes equations (convective form)
\\frac{\\partial \\mathbf{u}}{\\partial t} + (\\mathbf{u} \\cdot \\nabla) \\mathbf{u} -  \\nu \\nabla^2 \\mathbf{u} = - \\nabla w + \\mathbf{g}.

Velocity profile (laminar flow)

u(x) = 0, u(y) = u, u(z) = 0

for the y- direction, simplify Navier-Stokes equation

0 = -\\frac{\\mbox{d}P}{\\mbox{d}x} + \\mu\\left(\\frac{\\mbox{d}^2u}{\\mbox{d}y^2}\\right)

integrate twice to find velocity profile with boundary conditions: y = h, u = 0 y = -h, u = 0

u = \\frac{1}{2\\mu}\\left(\\frac{\\mbox{d}P}{\\mbox{d}x}\\right) y^2 + Ay + B

From this equation, sub in your two boundary conditions to get 2 equations

 0 = \\frac{1}{2 \\mu}\\frac{\\mathrm{d}P}{\\mathrm{d}x} h^2 + Ah + B 
 0 = \\frac{1}{2 \\mu}\\frac{\\mathrm{d}P}{\\mathrm{d}x} h^2 - Ah + B 

Add and solve for B

B = -\\frac{1}{2 \\mu}\\frac{\\mathrm{d}P}{\\mathrm{d}x} h^2

Substitute and solve for A

A = 0

Finally you get the velocity profile

u = \\frac{1}{2 \\mu}\\frac{\\mathrm{d}P}{\\mathrm{d}x}( y^2 - h^2 )

in tensor notation:

Incompressible Navier–Stokes equations (convective form)
\\left(\\frac{\\partial}{\\partial t}+u_j\\frac{\\partial}{\\partial x_j} - \\nu \\frac{\\partial^2}{\\partial x_j\\partial x_j} \\right) u_i = -\\frac{\\partial w}{\\partial x_i}+g_i 

where:

ν = 
μ
/
ρ0
 is the kinematic viscosity
It is well worth observing the meaning of each term (compare to the Cauchy momentum equation):


\\overbrace{
\\underbrace{\\frac{\\partial \\mathbf{u}}{\\partial t}}_{
\\begin{smallmatrix}
  \\text{Variation}
\\end{smallmatrix}} +
\\underbrace{(\\mathbf{u} \\cdot \\nabla) \\mathbf{u}}_{
\\begin{smallmatrix}
  \\text{Convection}
\\end{smallmatrix}}}^{\\text{Inertia (per volume)}}
\\overbrace{-\\underbrace{\\nu \\nabla^2 \\mathbf{u}}_{\\text{Diffusion}}=
\\underbrace{-\\nabla w}_{
\\begin{smallmatrix}
  \\text{Internal} \\\\
  \\text{source}
\\end{smallmatrix}}}^{\\text{Divergence of stress}} +
\\underbrace{\\mathbf{g}}_{
\\begin{smallmatrix}
  \\text{External} \\\\
  \\text{source}
\\end{smallmatrix}}
.
The higher-order term, namely the shear stress divergence ∇ ⋅ τ, has simply reduced to the vector laplacian term μ∇2u.[6] This laplacian term can be interpreted as the difference between the velocity at a point and the mean velocity in a small surrounding volume. This implies that – for a Newtonian fluid – viscosity operates as a diffusion of momentum, in much the same way as the heat conduction. In fact neglecting the convection term, incompressible Navier–Stokes equations lead to a vector diffusion equation (namely Stokes equations[disambiguation needed]), but in general the convection term is present, so incompressible Navier–Stokes equations belong to the class of convection-diffusion equations.

In the usual case of an external field being a conservative field:

 \\mathbf g = - \\nabla \\phi 
by defining the hydraulic head:

h \\equiv w + \\phi 
one can finally condense the whole source in one term, arriving to the incompressible Navier-Stokes equation with conservative external field:

\\frac{\\partial \\mathbf{u}}{\\partial t} + (\\mathbf{u} \\cdot \\nabla) \\mathbf{u} -  \\nu \\nabla^2 \\mathbf{u} = - \\nabla h.
The incompressible Navier–Stokes equations with conservative external field is the fundamental equation of hydraulics. The domain for these equations is commonly a 3 or less euclidean space, for which an orthogonal coordinate reference frame is usually set to explicit the system of scalar partial derivative equations to be solved. In 3D orthogonal coordinate systems are 3: Cartesian, cylindrical, and spherical. Expressing the Navier-Stokes vector equation in Cartesian coordinates is quite straightforward and not much influenced by the number of dimensions of the euclidean space employed, and this is the case also for the first-order terms (like the variation and convection ones) also in non-cartesian orthogonal coordinate systems. But for the higher order terms (the two coming from the divergence of the deviatoric stress that distinguish Navier–Stokes equations from Euler equations) some tensor calculus is required for deducing an expression in non-cartesian orthogonal coordinate systems.

The incompressible Navier–Stokes equation is composite, the sum of two orthogonal equations,

\\begin{align}
  \\frac{\\partial\\mathbf{u}}{\\partial t} &= \\Pi^S\\left(-(\\mathbf{u}\\cdot\\nabla)\\mathbf{u} + \\nu\\nabla^2\\mathbf{u}\\right) + \\mathbf{f}^S \\\\
                      \\rho^{-1}\\nabla p &= \\Pi^I\\left(-(\\mathbf{u}\\cdot\\nabla)\\mathbf{u} + \\nu\\nabla^2\\mathbf{u}\\right) + \\mathbf{f}^I
\\end{align}
where ΠS and ΠI are solenoidal and irrotational projection operators satisfying ΠS + ΠI = 1 and \\mathbf{f}^S and fI are the non-conservative and conservative parts of the body force. This result follows from the Helmholtz Theorem (also known as the fundamental theorem of vector calculus). The first equation is a pressureless governing equation for the velocity, while the second equation for the pressure is a functional of the velocity and is related to the pressure Poisson equation.

The explicit functional form of the projection operator in 3D is found from the Helmholtz Theorem:

\\Pi^S\\,\\mathbf{F}(\\mathbf{r}) = \\frac{1}{4\\pi}\\nabla\\times\\int \\frac{\\nabla^\\prime\\times\\mathbf{F}(\\mathbf{r}^\\prime)}{|\\mathbf{r}-\\mathbf{r}^\\prime|} d V^\\prime, \\quad \\Pi^I = 1-\\Pi^S
with a similar structure in 2D. Thus the governing equation is an integro-differential equation similar to Coulomb and Biot-Savart law, not convenient for numerical computation.

An equivalent weak or variational form of the equation, proved to produce the same velocity solution as the Navier–Stokes equation,[7] is given by,

\\left(\\mathbf{w},\\frac{\\partial\\mathbf{u}}{\\partial t}\\right) = -(\\mathbf{w},(\\mathbf{u}\\cdot\\nabla)\\mathbf{u})-\\nu(\\nabla\\mathbf{w}: \\nabla\\mathbf{u})+(\\mathbf{w},\\mathbf{f}^S)
for divergence-free test functions w satisfying appropriate boundary conditions. Here, the projections are accomplished by the orthogonality of the solenoidal and irrotational function spaces. The discrete form of this is imminently suited to finite element computation of divergence-free flow, as we shall see in the next section. There we will be able to address the question, "How does one specify pressure-driven (Poiseuille) problems with a pressureless governing equation?"

The absence of pressure forces from the governing velocity equation demonstrates that the equation is not a dynamic one, but rather a kinematic equation where the divergence-free condition serves the role of a conservation equation. This all would seem to refute the frequent statements that the incompressible pressure enforces the divergence-free condition.

Discrete velocity
With partitioning of the problem domain and defining basis functions on the partitioned domain, the discrete form of the governing equation is,

\\left(\\mathbf{w}_i, \\frac{\\partial\\mathbf{u}_j}{\\partial t}\\right) = -(\\mathbf{w}_i, (\\mathbf{u}\\cdot\\nabla)\\mathbf{u}_j) - \\nu(\\nabla\\mathbf{w}_i: \\nabla\\mathbf{u}_j) + \\left(\\mathbf{w}_i, \\mathbf{f}^S\\right).
It is desirable to choose basis functions which reflect the essential feature of incompressible flow – the elements must be divergence-free. While the velocity is the variable of interest, the existence of the stream function or vector potential is necessary by the Helmholtz Theorem. Further, to determine fluid flow in the absence of a pressure gradient, one can specify the difference of stream function values across a 2D channel, or the line integral of the tangential component of the vector potential around the channel in 3D, the flow being given by Stokes' Theorem. Discussion will be restricted to 2D in the following.

We further restrict discussion to continuous Hermite finite elements which have at least first-derivative degrees-of-freedom. With this, one can draw a large number of candidate triangular and rectangular elements from the plate-bending literature. These elements have derivatives as components of the gradient. In 2D, the gradient and curl of a scalar are clearly orthogonal, given by the expressions,

\\nabla\\phi = \\left[\\frac{\\partial \\phi}{\\partial x},\\,\\frac{\\partial \\phi}{\\partial y}\\right]^\\mathrm{T}, \\quad
\\nabla\\times\\phi = \\left[\\frac{\\partial \\phi}{\\partial y},\\,-\\frac{\\partial \\phi}{\\partial x}\\right]^\\mathrm{T}.
Adopting continuous plate-bending elements, interchanging the derivative degrees-of-freedom and changing the sign of the appropriate one gives many families of stream function elements.

Taking the curl of the scalar stream function elements gives divergence-free velocity elements.[8][9] The requirement that the stream function elements be continuous assures that the normal component of the velocity is continuous across element interfaces, all that is necessary for vanishing divergence on these interfaces.

Boundary conditions are simple to apply. The stream function is constant on no-flow surfaces, with no-slip velocity conditions on surfaces. Stream function differences across open channels determine the flow. No boundary conditions are necessary on open boundaries, though consistent values may be used with some problems. These are all Dirichlet conditions.

The algebraic equations to be solved are simple to set up, but of course are non-linear, requiring iteration of the linearized equations.

Similar considerations apply to three-dimensions, but extension from 2D is not immediate because of the vector nature of the potential, and there exists no simple relation between the gradient and the curl as was the case in 2D.

Pressure recovery
Recovering pressure from the velocity field is easy. The discrete weak equation for the pressure gradient is,

(\\mathbf{g}_i, \\nabla p) = -(\\mathbf{g}_i, (\\mathbf{u}\\cdot\\nabla)\\mathbf{u}_j) - \\nu(\\nabla\\mathbf{g}_i: \\nabla\\mathbf{u}_j) + (\\mathbf{g}_i, \\mathbf{f}^I)
where the test/weight functions are irrotational. Any conforming scalar finite element may be used. However, the pressure gradient field may also be of interest. In this case one can use scalar Hermite elements for the pressure. For the test/weight functions gi one would choose the irrotational vector elements obtained from the gradient of the pressure element.

Compressible flow
The Navier–Stokes equations result from the following assumptions on the stress tensor:[3]

the stress is Galileian invariant: it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient ∇u.
the stress is linear in this variable: σ(∇u) = C : (∇u), where C is the fourth-order tensor representing the constant of proportionality, called the viscosity or elasticity tensor, and : is the double-dot product.
the fluid is assumed to be isotropic, as with gases and simple liquids, and consequently \\mathbf  V is an isotropic tensor; furthermore, since the stress tensor is symmetric, by Helmholtz decomposition it can be expressed in terms of two scalar Lamé parameters, the bulk viscosity λ and the dynamic viscosity μ, as it is usual in linear elasticity:
Linear stress constitutive equation (expression used for elastic solid)
\\boldsymbol \\sigma = \\lambda (\\nabla\\cdot\\mathbf{u}) \\mathbf I + 2 \\mu \\boldsymbol \\varepsilon
where I is the identity tensor, ε(∇u) ≡ 
1
/
2
∇u + 
1
/
2
 (∇u)T is the rate-of-strain tensor and ∇ ⋅ u is the rate of expansion of the flow. So this decomposition can be explicited as:
\\boldsymbol \\sigma = \\lambda (\\nabla\\cdot\\mathbf{u}) \\mathbf I + \\mu (\\nabla\\mathbf{u} + \\left( \\nabla\\mathbf{u} \\right)^\\mathrm{T}).
Since the trace of the rate-of-strain tensor in three dimensions is:

\\mathrm{tr} (\\boldsymbol \\varepsilon) = \\nabla\\cdot\\mathbf{u}.
The trace of the stress tensor in three dimensions becomes:

\\mathrm{tr} (\\boldsymbol \\sigma) = (3 \\lambda + 2 \\mu )\\nabla\\cdot\\mathbf{u}.
So by alternatively decomposing the stress tensor is into isotropic and deviatoric parts, as usual in fluid dynamics:[10]

\\boldsymbol \\sigma = (\\lambda + \\tfrac23 \\mu) (\\nabla\\cdot\\mathbf{u})\\mathbf I + \\mu (\\nabla\\mathbf{u} + \\left( \\nabla\\mathbf{u} \\right)^\\mathrm{T} - \\tfrac23 (\\nabla\\cdot\\mathbf{u})\\mathbf I)
Introducing the second viscosity ζ,

  \\zeta \\equiv \\lambda + \\tfrac23 \\mu ,
we arrive to the linear constitutive equation in the form usually employed in thermal hydraulics:[3]

Linear stress constitutive equation (expression used for fluids)
\\boldsymbol \\sigma =  \\zeta  (\\nabla\\cdot\\mathbf{u}) \\mathbf I + \\mu (\\nabla\\mathbf{u} +  ( \\nabla\\mathbf{u} )^\\mathrm{T} - \\tfrac23 (\\nabla\\cdot\\mathbf{u})\\mathbf I)
Both bulk viscosity λ and dynamic viscosity μ need not be constant – in general, they depend on density, on each other (the viscosity is expressed in pressure), and in compressible flows also on temperature. Any equation expliciting one of these transport coefficient in the conservation variables is called an equation of state.[4]

By computing the divergence of the stress tensor, since the divergence of tensor ∇u is ∇2u and the divergence of tensor (∇u)T is ∇(∇ ⋅ u)., one finally arrives to the compressible (most general) Navier-Stokes momentum equation:[11]

Navier-Stokes momentum equation (convective form)
 \\frac{\\partial \\mathbf{u}}{\\partial t} + \\mathbf{u} \\cdot \\nabla \\mathbf{u}= -\\frac 1 \\rho \\nabla \\bar{p} + \\nu \\nabla^2 \\mathbf u + \\tfrac13 \\, \\nu \\nabla (\\nabla\\cdot\\mathbf{u}) + \\mathbf{g} .

Bulk viscosity is assumed to be constant, otherwise it should not be taken out of the last derivative. The effect of the volume viscosity ζ is that the mechanical pressure is not equivalent to the thermodynamic pressure:[12]

  \\bar{p} \\equiv p - \\zeta \\nabla \\cdot  \\mathbf{u}  ,
This difference is usually neglected, sometimes by explicitly assuming ζ = 0, but it could have an impact in sound absorption and attenuation and shock waves , see .[13]

For the special case of an incompressible flow, the pressure constrains the flow so that the volume of fluid elements is constant: isochoric flow resulting in a solenoidal velocity field with ∇ ⋅ u = 0.[14]
""".lower()


# In[9]:


print(naive_multi_search(patterns,rawtext)==aho_corasick(patterns,rawtext))


# In[10]:


#55.7 ms ± 839 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
get_ipython().run_line_magic('timeit', 'naive_multi_search(patterns,rawtext)')


# In[11]:


#24.2 ms ± 571 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
#ac is significantly faster than naïve!
get_ipython().run_line_magic('timeit', 'aho_corasick(patterns,rawtext)')

