<div align=justify>

# Recent Changes

- Added documentation for commands

# Next Tasks:

- Finalise sample data and add documentation for it (in readme) so that it is easy to understand what entries already exist and how they relate to one another

- Review:
    - Determine if more commands are necessary
    - Ensure error checking is done for all processes
    - Ensure controllers are organised

# Notes
• Employers and students can be created without pre-existing data, however Staff can only be created after their Employer has been created. This is because staff are associated with their employer since they can only shortlist students for positions created by their employer, thus staff cannot exist without employer

- The command list table below outlines 'desireable' requirements:
    - These requirements are **already met** by sample data and do not need to be fulfilled
    - As the name implies, these are 'soft' requirements. In other words, the system will be able to function even when these requrements aren't met. These requirements are simply outlined for a desireable outcome (list commands show data, avoiding prompts such as 'Student not shortlisted for any position', etc.) and serve as guidelines if all entries from all tables are deleted so that it can be created from scratch

- This CLI **does not** use click arguments. After entering a command you will be prompted if more information is needed
</div>

# Command List

| Command  | Model | Prompts | Description | Desireable Requirements |
| :---: | :---: | :---: | :---: | :---: |
| flask employer list | employer | None | Lists all employers | At least one employer exists |
| flask employer create | employer | Username, Password, Company Name | Creates employer | None |
| flask employer view-positions | employer | UserID |View positions created by a specified employer | At least one employer who has created at least one position already exists |
| flask staff list | staff | None | Lists all staff | At least one staff member exists |
| flask staff create | staff | EmployerID, Username, Password | Creates staff | The employer that staff is to be assigned to exists |
| flask staff add-to-shortlist | staff | StaffID, PositionID, StudentID | Adds a student to a shortlist | At least one student who does not belong to the target shortlist exists |
| flask student list | student | None | Lists all students | At least one student exists |
| flask student create | student | Username, Password, Faculty, Department, Degree, GPA | Creates student | None |
| flask student view-shortlists | student | StudentID | Lists positions student has been shortlisted for, including details such as the status and the employer response | At least one student who has been shortlisted exists |
