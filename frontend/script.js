// function startProfile() {
//     window.location.href = "profile.html";
// }


// /* =========================
//    CREATE STUDENT PROFILE
//    ========================= */

// const profileForm = document.getElementById("profileForm");

// if (profileForm) {

//     profileForm.addEventListener("submit", async function (event) {

//         event.preventDefault();

//         const message = document.getElementById("message");

//         const skillsInput = document.getElementById("skills").value;

//         const skills = skillsInput
//             .split(",")
//             .map(skill => skill.trim())
//             .filter(skill => skill !== "");


//         const profileData = {

//             name: document.getElementById("name").value,

//             email: document.getElementById("email").value,

//             education: [
//                 {
//                     degree: document.getElementById("degree").value,

//                     institution: document.getElementById("institution").value,

//                     graduation_year: Number(
//                         document.getElementById("graduation_year").value
//                     )
//                 }
//             ],

//             skills: skills,

//             certifications: [],

//             projects: [],

//             target_job_role:
//                 document.getElementById("target_job_role").value
//         };


//         try {

//             const response = await fetch(
//                 "http://127.0.0.1:8000/students/profile",
//                 {
//                     method: "POST",

//                     headers: {
//                         "Content-Type": "application/json"
//                     },

//                     body: JSON.stringify(profileData)
//                 }
//             );


//             const data = await response.json();


//             if (response.ok) {

//                 window.location.href =
//                     "analysis.html?student_id=" +
//                     encodeURIComponent(data.student_id);

//             } else {

//                 message.textContent =
//                     data.detail || "Failed to create profile.";

//                 message.style.color = "red";
//             }


//         } catch (error) {

//             console.error(error);

//             message.textContent =
//                 "Could not connect to the backend.";

//             message.style.color = "red";
//         }

//     });

// }


// /* =========================
//    SKILL ANALYSIS
//    ========================= */

// const matchPercentage =
//     document.getElementById("matchPercentage");


// if (matchPercentage) {

//     const params = new URLSearchParams(
//         window.location.search
//     );

//     const studentId = params.get("student_id");


//     if (!studentId) {

//         document.getElementById("analysisMessage").textContent =
//             "Student ID not found.";

//     } else {

//         loadAnalysis(studentId);

//     }
// }


// async function loadAnalysis(studentId) {

//     try {

//         const response = await fetch(
//             "http://127.0.0.1:8000/students/" +
//             encodeURIComponent(studentId) +
//             "/analysis"
//         );


//         const data = await response.json();


//         if (!response.ok) {

//             throw new Error(
//                 data.detail || "Failed to load analysis."
//             );

//         }


//         document.getElementById("matchPercentage").textContent =
//             data.match_percentage + "%";


//         displaySkills(
//             "currentSkills",
//             data.current_skills
//         );


//         displaySkills(
//             "requiredSkills",
//             data.required_skills
//         );


//         displaySkills(
//             "missingSkills",
//             data.missing_skills,
//             true
//         );


//     } catch (error) {

//         console.error(error);

//         document.getElementById("analysisMessage").textContent =
//             error.message;

//     }

// }


// /* =========================
//    JOB RECOMMENDATIONS
//    ========================= */

// const jobsContainer =
//     document.getElementById("jobsContainer");


// if (jobsContainer) {

//     const params = new URLSearchParams(
//         window.location.search
//     );

//     const studentId = params.get("student_id");


//     if (!studentId) {

//         document.getElementById("jobsMessage").textContent =
//             "Student ID not found.";

//     } else {

//         loadJobs(studentId);

//     }

// }


// async function loadJobs(studentId) {

//     try {

//         const response = await fetch(
//             "http://127.0.0.1:8000/jobs/recommendations/" +
//             encodeURIComponent(studentId)
//         );


//         const data = await response.json();


//         if (!response.ok) {

//             throw new Error(
//                 data.detail || "Failed to load jobs."
//             );

//         }


//         const jobs = data.jobs || [];


//         const message =
//             document.getElementById("jobsMessage");


//         if (jobs.length === 0) {

//             message.textContent =
//                 "No matching jobs found.";

//             return;

//         }


//         message.textContent =
//             jobs.length + " job(s) found";


//         jobsContainer.innerHTML = "";


//         jobs.forEach(function (job) {

//             const jobCard =
//                 document.createElement("div");

//             jobCard.classList.add("job-card");


//             const skillsHtml =
//                 createJobSkills(
//                     job.required_skills
//                 );


//             const missingSkillsHtml =
//                 createJobSkills(
//                     job.missing_skills,
//                     true
//                 );


//             jobCard.innerHTML = `

//                 <h2>${job.title || "Job Title"}</h2>

//                 <p class="job-company">
//                     ${job.company || "Company not specified"}
//                 </p>

//                 <p class="job-location">
//                     ${job.location || "Location not specified"}
//                 </p>

//                 <p class="job-match">
//                     Match: ${job.match_percentage}%
//                 </p>

//                 <h3>Required Skills</h3>

//                 <div class="job-skills">
//                     ${skillsHtml}
//                 </div>

//                 <h3>Missing Skills</h3>

//                 <div class="job-skills">
//                     ${missingSkillsHtml || "None"}
//                 </div>

//                 <a
//                     href="${job.apply_url || "#"}"
//                     target="_blank"
//                     class="apply-button"
//                 >
//                     Apply Now
//                 </a>

//             `;


//             jobsContainer.appendChild(jobCard);

//         });


//     } catch (error) {

//         console.error(error);

//         document.getElementById("jobsMessage").textContent =
//             error.message;

//     }

// }


// /* =========================
//    JOB SKILL DISPLAY
//    ========================= */

// function createJobSkills(
//     skills,
//     missing = false
// ) {

//     if (!skills || skills.length === 0) {

//         return "";

//     }


//     return skills.map(function (skill) {

//         return `
//             <span class="job-skill ${
//                 missing ? "job-missing-skill" : ""
//             }">
//                 ${skill}
//             </span>
//         `;

//     }).join("");

// }


// /* =========================
//    GENERAL SKILL DISPLAY
//    ========================= */

// function displaySkills(
//     elementId,
//     skills,
//     missing = false
// ) {

//     const container =
//         document.getElementById(elementId);


//     container.innerHTML = "";


//     if (!skills || skills.length === 0) {

//         container.textContent =
//             "No skills found.";

//         return;

//     }


//     skills.forEach(function (skill) {

//         const span =
//             document.createElement("span");


//         span.textContent = skill;

//         span.classList.add("skill-item");


//         if (missing) {

//             span.classList.add("missing-skill");

//         }


//         container.appendChild(span);

//     });

// }
// function goToJobs() {

//     const params = new URLSearchParams(
//         window.location.search
//     );

//     const studentId = params.get("student_id");


//     if (!studentId) {

//         alert("Student ID not found.");

//         return;
//     }


//     window.location.href =
//         "jobs.html?student_id=" +
//         encodeURIComponent(studentId);
// }
function startProfile() {
    window.location.href = "profile.html";
}


/* =========================
   CREATE STUDENT PROFILE
   ========================= */
async function submitProfile(event) {

    event.preventDefault();

    const message = document.getElementById("message");

    message.textContent = "Creating your profile...";
    message.style.color = "#60a5fa";


    const skillsInput =
        document.getElementById("skills").value;

    const skills = skillsInput
        .split(",")
        .map(skill => skill.trim())
        .filter(skill => skill !== "");


    const profileData = {

        name:
            document.getElementById("name").value,

        email:
            document.getElementById("email").value,

        education: [
            {
                degree:
                    document.getElementById("degree").value,

                institution:
                    document.getElementById("institution").value,

                graduation_year:
                    Number(
                        document.getElementById(
                            "graduation_year"
                        ).value
                    )
            }
        ],

        skills: skills,

        certifications: [],

        projects: [],

        target_job_role:
            document.getElementById(
                "target_job_role"
            ).value
    };


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/students/profile",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(profileData)
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Failed to create profile."
            );

        }


        window.location.href =
            "analysis.html?student_id=" +
            encodeURIComponent(
                data.student_id
            );


    } catch (error) {

        console.error(error);

        message.textContent =
            error.message;

        message.style.color = "#f87171";
    }

}




const profileForm = document.getElementById("profileForm");

if (profileForm) {

    profileForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const message = document.getElementById("message");

        const skillsInput = document.getElementById("skills").value;

        const skills = skillsInput
            .split(",")
            .map(skill => skill.trim())
            .filter(skill => skill !== "");


        const profileData = {

            name: document.getElementById("name").value,

            email: document.getElementById("email").value,

            education: [
                {
                    degree: document.getElementById("degree").value,

                    institution: document.getElementById("institution").value,

                    graduation_year: Number(
                        document.getElementById("graduation_year").value
                    )
                }
            ],

            skills: skills,

            certifications: [],

            projects: [],

            target_job_role:
                document.getElementById("target_job_role").value
        };


        try {

            const response = await fetch(
                "http://127.0.0.1:8000/students/profile",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(profileData)
                }
            );


            const data = await response.json();


            if (response.ok) {

                window.location.href =
                    "analysis.html?student_id=" +
                    encodeURIComponent(data.student_id);

            } else {

                message.textContent =
                    data.detail || "Failed to create profile.";

                message.style.color = "red";
            }


        } catch (error) {

            console.error(error);

            message.textContent =
                "Could not connect to the backend.";

            message.style.color = "red";
        }

    });

}


/* =========================
   SKILL ANALYSIS
   ========================= */

const matchPercentage =
    document.getElementById("matchPercentage");


if (matchPercentage) {

    const params = new URLSearchParams(
        window.location.search
    );

    const studentId = params.get("student_id");


    if (!studentId) {

        document.getElementById("analysisMessage").textContent =
            "Student ID not found.";

    } else {

        loadAnalysis(studentId);

    }

}


async function loadAnalysis(studentId) {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/students/" +
            encodeURIComponent(studentId) +
            "/analysis"
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail || "Failed to load analysis."
            );

        }


        document.getElementById("matchPercentage").textContent =
            data.match_percentage + "%";


        displaySkills(
            "currentSkills",
            data.current_skills
        );


        displaySkills(
            "requiredSkills",
            data.required_skills
        );


        displaySkills(
            "missingSkills",
            data.missing_skills,
            true
        );


    } catch (error) {

        console.error(error);

        document.getElementById("analysisMessage").textContent =
            error.message;

    }

}


/* =========================
   JOB RECOMMENDATIONS
   ========================= */

const jobsContainer =
    document.getElementById("jobsContainer");


if (jobsContainer) {

    const params = new URLSearchParams(
        window.location.search
    );

    const studentId = params.get("student_id");


    if (!studentId) {

        document.getElementById("jobsMessage").textContent =
            "Student ID not found.";

    } else {

        loadJobs(studentId);

    }

}


async function loadJobs(studentId) {

    try {

        /*
         * Each student has a separate page counter.
         */

        const pageKey =
            "jobPage_" + studentId;


        let page = Number(
            localStorage.getItem(pageKey)
        ) || 1;


        /*
         * Request only 3 jobs.
         */

        const response = await fetch(
            "http://127.0.0.1:8000/jobs/recommendations/" +
            encodeURIComponent(studentId) +
            "?limit=3&page=" +
            page
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail || "Failed to load jobs."
            );

        }


        const jobs = data.jobs || [];

        const message =
            document.getElementById("jobsMessage");


        if (jobs.length === 0) {

            message.textContent =
                "No more jobs found.";

            return;

        }


        message.textContent =
            jobs.length + " more job(s) found";


        /*
         * IMPORTANT:
         * We do NOT clear jobsContainer.
         * New jobs are added below existing jobs.
         */

        jobs.forEach(function (job) {

            const jobCard =
                document.createElement("div");

            jobCard.classList.add("job-card");


            const skillsHtml =
                createJobSkills(
                    job.required_skills
                );


            const missingSkillsHtml =
                createJobSkills(
                    job.missing_skills,
                    true
                );


            jobCard.innerHTML = `

                <h2>${job.title || "Job Title"}</h2>

                <p class="job-company">
                    ${job.company || "Company not specified"}
                </p>

                <p class="job-location">
                    ${job.location || "Location not specified"}
                </p>

                <p class="job-match">
                    Match: ${job.match_percentage}%
                </p>

                <h3>Required Skills</h3>

                <div class="job-skills">
                    ${skillsHtml || "No skills found"}
                </div>

                <h3>Missing Skills</h3>

                <div class="job-skills">
                    ${missingSkillsHtml || "None"}
                </div>

                <a
                    href="${job.apply_url || "#"}"
                    target="_blank"
                    class="apply-button"
                >
                    Apply Now
                </a>

            `;


            jobsContainer.appendChild(jobCard);

        });


        /*
         * Store the next page number.
         */

        localStorage.setItem(
            pageKey,
            page + 1
        );


    } catch (error) {

        console.error(error);

        document.getElementById("jobsMessage").textContent =
            error.message;

    }

}


/* =========================
   REFRESH JOBS
   ========================= */

function refreshJobs() {

    const params = new URLSearchParams(
        window.location.search
    );

    const studentId = params.get("student_id");

    if (!studentId) {
        alert("Student ID not found.");
        return;
    }

    const button =
        document.getElementById("refreshButton");

    button.textContent = "Loading...";
    button.disabled = true;

    loadJobs(studentId)
        .finally(function () {

            setTimeout(function () {

                button.textContent = "Load More Jobs";
                button.disabled = false;

            }, 800);

        });

}

/* =========================
   JOB SKILL DISPLAY
   ========================= */

function createJobSkills(
    skills,
    missing = false
) {

    if (!skills || skills.length === 0) {

        return "";

    }


    return skills.map(function (skill) {

        return `
            <span class="job-skill ${
                missing ? "job-missing-skill" : ""
            }">
                ${skill}
            </span>
        `;

    }).join("");

}


/* =========================
   GENERAL SKILL DISPLAY
   ========================= */

function displaySkills(
    elementId,
    skills,
    missing = false
) {

    const container =
        document.getElementById(elementId);


    container.innerHTML = "";


    if (!skills || skills.length === 0) {

        container.textContent =
            "No skills found.";

        return;

    }


    skills.forEach(function (skill) {

        const span =
            document.createElement("span");


        span.textContent = skill;

        span.classList.add("skill-item");


        if (missing) {

            span.classList.add("missing-skill");

        }


        container.appendChild(span);

    });

}


/* =========================
   GO TO JOBS
   ========================= */

function goToJobs() {

    const params = new URLSearchParams(
        window.location.search
    );

    const studentId = params.get("student_id");


    if (!studentId) {

        alert("Student ID not found.");

        return;

    }


    window.location.href =
        "jobs.html?student_id=" +
        encodeURIComponent(studentId);

}