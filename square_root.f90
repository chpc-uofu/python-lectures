! Fortran example
program main

    implicit none
    double precision :: x = 17.0

    write(*,'(A,F8.4,A,F12.6)') "The square root of ", x, " is ", sqrt(x)

end program     