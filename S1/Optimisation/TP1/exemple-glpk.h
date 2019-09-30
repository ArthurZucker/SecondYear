/*
 *  exemple-glpk.h
 *  glpk-teaching
 *
 *  Created by Ouzia on 02/05/10.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <glpk.h>

/*-----
 * LP_PRIMAL: 
 *------------------
 *
 * In this example, we will solve (using GLPK simplex algorithm) the following 
 * linear programming problem: 
 * 
 *   Maximize 3x1 + 5x2 + 7x3
 *       s.t. 
 *            2x1 + 2x2 +  x3 <= 4
 *             x1 + 3x2 +  x3 <= 3
 *            4x1 +  x2 + 2x3 <= 5 
 *             x1,   x2, x3 >= 0 
 *
 * Also, it shows how one can get back different information about
 * the solution found. 
 *
 *----------------------------------------------------------------------------*/
int exemple_glpk(int argc, const char * argv[]);