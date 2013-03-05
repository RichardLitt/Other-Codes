me of the primary .tex file:
MAIN="main"

function do_cleanup {
   rm -f ${MAIN}.bbl ${MAIN}.blg ${MAIN}.log ${MAIN}.toc ${MAIN}.idx \
               ${MAIN}.ilg ${MAIN}.ind ${MAIN}.aux
 }

 function die {
    do_cleanup
       rm "${MAIN}.pdf"
          echo "* ERROR: $1 *"
             exit 1
           }

           function do_pdflatex {
              pdflatex -halt-on-error -file-line-error-style $* || die "pdflatex exited with an error."
            }

            # Compile LaTeX -> pdf:
          do_pdflatex ${MAIN} && bibtex ${MAIN} && do_pdflatex ${MAIN} \
            && echo -e "\n\n\n\n\n\nFinal LaTeX output:" \
            && do_pdflatex ${MAIN}

        do_cleanup
