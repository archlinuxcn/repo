      PROGRAM EXAMPLE1
*
*     Example Program solving Ax=b via ScaLAPACK routine PDGESV
*
*     .. Parameters ..
      INTEGER            DLEN_, IA, JA, IB, JB, M, N, MB, NB, RSRC,
     $                   CSRC, MXLLDA, MXLLDB, NRHS, NBRHS, NOUT,
     $                   MXLOCR, MXLOCC, MXRHSC
      PARAMETER          ( DLEN_ = 9, IA = 1, JA = 1, IB = 1, JB = 1,
     $                   M = 9, N = 9, MB = 2, NB = 2, RSRC = 0,
     $                   CSRC = 0, MXLLDA = 5, MXLLDB = 5, NRHS = 1,
     $                   NBRHS = 1, NOUT = 6, MXLOCR = 5, MXLOCC = 4,
     $                   MXRHSC = 1 )
      DOUBLE PRECISION   ONE
      PARAMETER          ( ONE = 1.0D+0 )
*     ..
*     .. Local Scalars ..
      INTEGER            ICTXT, INFO, MYCOL, MYROW, NPCOL, NPROW
      DOUBLE PRECISION   ANORM, BNORM, EPS, RESID, XNORM
*     ..
*     .. Local Arrays ..
      INTEGER            DESCA( DLEN_ ), DESCB( DLEN_ ),
     $                   IPIV( MXLOCR+NB )
      DOUBLE PRECISION   A( MXLLDA, MXLOCC ), A0( MXLLDA, MXLOCC ),
     $                   B( MXLLDB, MXRHSC ), B0( MXLLDB, MXRHSC ),
     $                   WORK( MXLOCR )
*     ..
*     .. External Functions ..
      DOUBLE PRECISION   PDLAMCH, PDLANGE
      EXTERNAL           PDLAMCH, PDLANGE
*     ..
*     .. External Subroutines ..
      EXTERNAL           BLACS_EXIT, BLACS_GRIDEXIT, BLACS_GRIDINFO,
     $                   DESCINIT, MATINIT, PDGEMM, PDGESV, PDLACPY,
     $                   SL_INIT
*     ..
*     .. Intrinsic Functions ..
      INTRINSIC          DBLE
*     ..
*     .. Data statements ..
      DATA               NPROW / 2 / , NPCOL / 3 /
*     ..
*     .. Executable Statements ..
*
*     INITIALIZE THE PROCESS GRID
*
      CALL SL_INIT( ICTXT, NPROW, NPCOL )
      CALL BLACS_GRIDINFO( ICTXT, NPROW, NPCOL, MYROW, MYCOL )
*
*     If I'm not in the process grid, go to the end of the program
*
      IF( MYROW.EQ.-1 )
     $   GO TO 10
*
*     DISTRIBUTE THE MATRIX ON THE PROCESS GRID
*     Initialize the array descriptors for the matrices A and B
*
      CALL DESCINIT( DESCA, M, N, MB, NB, RSRC, CSRC, ICTXT, MXLLDA,
     $               INFO )
      CALL DESCINIT( DESCB, N, NRHS, NB, NBRHS, RSRC, CSRC, ICTXT,
     $               MXLLDB, INFO )
*
*     Generate matrices A and B and distribute to the process grid
*
      CALL MATINIT( A, DESCA, B, DESCB )
*
*     Make a copy of A and B for checking purposes
*
      CALL PDLACPY( 'All', N, N, A, 1, 1, DESCA, A0, 1, 1, DESCA )
      CALL PDLACPY( 'All', N, NRHS, B, 1, 1, DESCB, B0, 1, 1, DESCB )
*
*     CALL THE SCALAPACK ROUTINE
*     Solve the linear system A * X = B
*
      CALL PDGESV( N, NRHS, A, IA, JA, DESCA, IPIV, B, IB, JB, DESCB,
     $             INFO )
*
      IF( MYROW.EQ.0 .AND. MYCOL.EQ.0 ) THEN
         WRITE( NOUT, FMT = 9999 )
         WRITE( NOUT, FMT = 9998 )M, N, NB
         WRITE( NOUT, FMT = 9997 )NPROW*NPCOL, NPROW, NPCOL
         WRITE( NOUT, FMT = 9996 )INFO
      END IF
*
*     Compute residual ||A * X  - B|| / ( ||X|| * ||A|| * eps * N )
*
      EPS = PDLAMCH( ICTXT, 'Epsilon' )
      ANORM = PDLANGE( 'I', N, N, A, 1, 1, DESCA, WORK )
      BNORM = PDLANGE( 'I', N, NRHS, B, 1, 1, DESCB, WORK )
      CALL PDGEMM( 'N', 'N', N, NRHS, N, ONE, A0, 1, 1, DESCA, B, 1, 1,
     $             DESCB, -ONE, B0, 1, 1, DESCB )
      XNORM = PDLANGE( 'I', N, NRHS, B0, 1, 1, DESCB, WORK )
      RESID = XNORM / ( ANORM*BNORM*EPS*DBLE( N ) )
*
      IF( MYROW.EQ.0 .AND. MYCOL.EQ.0 ) THEN
         IF( RESID.LT.10.0D+0 ) THEN
            WRITE( NOUT, FMT = 9995 )
            WRITE( NOUT, FMT = 9993 )RESID
         ELSE
            WRITE( NOUT, FMT = 9994 )
            WRITE( NOUT, FMT = 9993 )RESID
         END IF
      END IF
*
*     RELEASE THE PROCESS GRID
*     Free the BLACS context
*
      CALL BLACS_GRIDEXIT( ICTXT )
   10 CONTINUE
*
*     Exit the BLACS
*
      CALL BLACS_EXIT( 0 )
*
 9999 FORMAT( / 'ScaLAPACK Example Program #1 -- May 1, 1997' )
 9998 FORMAT( / 'Solving Ax=b where A is a ', I3, ' by ', I3,
     $      ' matrix with a block size of ', I3 )
 9997 FORMAT( 'Running on ', I3, ' processes, where the process grid',
     $      ' is ', I3, ' by ', I3 )
 9996 FORMAT( / 'INFO code returned by PDGESV = ', I3 )
 9995 FORMAT( /
     $   'According to the normalized residual the solution is correct.'
     $       )
 9994 FORMAT( /
     $ 'According to the normalized residual the solution is incorrect.'
     $       )
 9993 FORMAT( / '||A*x - b|| / ( ||x||*||A||*eps*N ) = ', 1P, E16.8 )
      STOP
      END
      SUBROUTINE MATINIT( AA, DESCA, B, DESCB )
*
*     MATINIT generates and distributes matrices A and B (depicted in
*     Figures 2.5 and 2.6) to a 2 x 3 process grid
*
*     .. Array Arguments ..
      INTEGER            DESCA( * ), DESCB( * )
      DOUBLE PRECISION   AA( * ), B( * )
*     ..
*     .. Parameters ..
      INTEGER            CTXT_, LLD_
      PARAMETER          ( CTXT_ = 2, LLD_ = 9 )
*     ..
*     .. Local Scalars ..
      INTEGER            ICTXT, MXLLDA, MYCOL, MYROW, NPCOL, NPROW
      DOUBLE PRECISION   A, C, K, L, P, S
*     ..
*     .. External Subroutines ..
      EXTERNAL           BLACS_GRIDINFO
*     ..
*     .. Executable Statements ..
*
      ICTXT = DESCA( CTXT_ )
      CALL BLACS_GRIDINFO( ICTXT, NPROW, NPCOL, MYROW, MYCOL )
*
      S = 19.0D0
      C = 3.0D0
      A = 1.0D0
      L = 12.0D0
      P = 16.0D0
      K = 11.0D0
*
      MXLLDA = DESCA( LLD_ )
*
      IF( MYROW.EQ.0 .AND. MYCOL.EQ.0 ) THEN
         AA( 1 ) = S
         AA( 2 ) = -S
         AA( 3 ) = -S
         AA( 4 ) = -S
         AA( 5 ) = -S
         AA( 1+MXLLDA ) = C
         AA( 2+MXLLDA ) = C
         AA( 3+MXLLDA ) = -C
         AA( 4+MXLLDA ) = -C
         AA( 5+MXLLDA ) = -C
         AA( 1+2*MXLLDA ) = A
         AA( 2+2*MXLLDA ) = A
         AA( 3+2*MXLLDA ) = A
         AA( 4+2*MXLLDA ) = A
         AA( 5+2*MXLLDA ) = -A
         AA( 1+3*MXLLDA ) = C
         AA( 2+3*MXLLDA ) = C
         AA( 3+3*MXLLDA ) = C
         AA( 4+3*MXLLDA ) = C
         AA( 5+3*MXLLDA ) = -C
         B( 1 ) = 0.0D0
         B( 2 ) = 0.0D0
         B( 3 ) = 0.0D0
         B( 4 ) = 0.0D0
         B( 5 ) = 0.0D0
      ELSE IF( MYROW.EQ.0 .AND. MYCOL.EQ.1 ) THEN
         AA( 1 ) = A
         AA( 2 ) = A
         AA( 3 ) = -A
         AA( 4 ) = -A
         AA( 5 ) = -A
         AA( 1+MXLLDA ) = L
         AA( 2+MXLLDA ) = L
         AA( 3+MXLLDA ) = -L
         AA( 4+MXLLDA ) = -L
         AA( 5+MXLLDA ) = -L
         AA( 1+2*MXLLDA ) = K
         AA( 2+2*MXLLDA ) = K
         AA( 3+2*MXLLDA ) = K
         AA( 4+2*MXLLDA ) = K
         AA( 5+2*MXLLDA ) = K
      ELSE IF( MYROW.EQ.0 .AND. MYCOL.EQ.2 ) THEN
         AA( 1 ) = A
         AA( 2 ) = A
         AA( 3 ) = A
         AA( 4 ) = -A
         AA( 5 ) = -A
         AA( 1+MXLLDA ) = P
         AA( 2+MXLLDA ) = P
         AA( 3+MXLLDA ) = P
         AA( 4+MXLLDA ) = P
         AA( 5+MXLLDA ) = -P
      ELSE IF( MYROW.EQ.1 .AND. MYCOL.EQ.0 ) THEN
         AA( 1 ) = -S
         AA( 2 ) = -S
         AA( 3 ) = -S
         AA( 4 ) = -S
         AA( 1+MXLLDA ) = -C
         AA( 2+MXLLDA ) = -C
         AA( 3+MXLLDA ) = -C
         AA( 4+MXLLDA ) = C
         AA( 1+2*MXLLDA ) = A
         AA( 2+2*MXLLDA ) = A
         AA( 3+2*MXLLDA ) = A
         AA( 4+2*MXLLDA ) = -A
         AA( 1+3*MXLLDA ) = C
         AA( 2+3*MXLLDA ) = C
         AA( 3+3*MXLLDA ) = C
         AA( 4+3*MXLLDA ) = C
         B( 1 ) = 1.0D0
         B( 2 ) = 0.0D0
         B( 3 ) = 0.0D0
         B( 4 ) = 0.0D0
      ELSE IF( MYROW.EQ.1 .AND. MYCOL.EQ.1 ) THEN
         AA( 1 ) = A
         AA( 2 ) = -A
         AA( 3 ) = -A
         AA( 4 ) = -A
         AA( 1+MXLLDA ) = L
         AA( 2+MXLLDA ) = L
         AA( 3+MXLLDA ) = -L
         AA( 4+MXLLDA ) = -L
         AA( 1+2*MXLLDA ) = K
         AA( 2+2*MXLLDA ) = K
         AA( 3+2*MXLLDA ) = K
         AA( 4+2*MXLLDA ) = K
      ELSE IF( MYROW.EQ.1 .AND. MYCOL.EQ.2 ) THEN
         AA( 1 ) = A
         AA( 2 ) = A
         AA( 3 ) = -A
         AA( 4 ) = -A
         AA( 1+MXLLDA ) = P
         AA( 2+MXLLDA ) = P
         AA( 3+MXLLDA ) = -P
         AA( 4+MXLLDA ) = -P
      END IF
      RETURN
      END
      SUBROUTINE SL_INIT( ICTXT, NPROW, NPCOL )
*
*     .. Scalar Arguments ..
      INTEGER            ICTXT, NPCOL, NPROW
*     ..
*
*  Purpose
*  =======
*
*  SL_INIT initializes an NPROW x NPCOL process grid using a row-major
*  ordering  of  the  processes. This routine retrieves a default system
*  context  which  will  include all available processes. In addition it
*  spawns the processes if needed.
*
*  Arguments
*  =========
*
*  ICTXT   (global output) INTEGER
*          ICTXT specifies the BLACS context handle identifying the
*          created process grid.  The context itself is global.
*
*  NPROW   (global input) INTEGER
*          NPROW specifies the number of process rows in the grid
*          to be created.
*
*  NPCOL   (global input) INTEGER
*          NPCOL specifies the number of process columns in the grid
*          to be created.
*
*  =====================================================================
*
*     .. Local Scalars ..
      INTEGER            IAM, NPROCS
*     ..
*     .. External Subroutines ..
      EXTERNAL           BLACS_GET, BLACS_GRIDINIT, BLACS_PINFO,
     $                   BLACS_SETUP
*     ..
*     .. Executable Statements ..
*
*     Get starting information
*
      CALL BLACS_PINFO( IAM, NPROCS )
*
*     If machine needs additional set up, do it now
*
      IF( NPROCS.LT.1 ) THEN
         IF( IAM.EQ.0 )
     $      NPROCS = NPROW*NPCOL
         CALL BLACS_SETUP( IAM, NPROCS )
      END IF
*
*     Define process grid
*
      CALL BLACS_GET( -1, 0, ICTXT )
      CALL BLACS_GRIDINIT( ICTXT, 'Row-major', NPROW, NPCOL )
*
      RETURN
*
*     End of SL_INIT
*
      END
