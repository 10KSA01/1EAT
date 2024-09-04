# Inspiration
Many global companies contribute to climate change and the ever-increasing levels of carbon emissions. Our tool is designed to help these companies reduce their carbon footprint and their carbon tax each year.

# What It Does
We provide a web app dashboard that allows companies to view their historical carbon data in relation to their revenue and profit. This enables them to identify what they need to do to avoid exceeding their carbon credit budget, with the assistance of MATLAB analysis. We use Auth0 for credential management, allowing both company managers and analysis teams to log in effortlessly. Additionally, we utilize Twilio to enable users to set up alerts when the tool predicts that the company is consuming excessive carbon. MATLAB is employed in the backend to analyze the large datasets provided by the companies.

# How We Built It
We ventured into new territory by using Python as our web server. Python interacts with various components, including public APIs and graphing libraries. The web server is powered by the Flask framework, which is enhanced with Dash, providing an easy interface to display Plotly graphs and charts. These graphs are what users interact with most, and we designed them to be as readable as possible while accurately portraying the desired data.

# Challenges We Encountered
Having never used Python for such a project, we worked diligently to read documentation, evaluate competing libraries, and debug our code. To be honest, it was more than we initially anticipated, but we succeeded in creating a tool that can help improve the environment by enabling companies to identify areas where they are falling behind.

# Accomplishments We’re Proud Of
Our team originally consisted of three software engineers. During the event, we welcomed two additional members: a physics major with an interest in coding and hackathons, and a UI/UX designer. We collaborated with individuals from non-coding backgrounds to produce an accurate data interface that is also aesthetically pleasing. Creating a web app using Python for the first time is an accomplishment we take great pride in. The framework we utilized, Dash, is an enterprise-level library that typically requires training to use in industry. We managed to find solutions with minimal training and in a short amount of time.

# What We Learned
We learned the importance of collaboration with diverse team members. Our UI/UX designer took on significant responsibilities, designing an interface informed by their understanding of how users would interact with the web app. The programmers then implemented this design, fostering new communication dynamics that we found very beneficial. We also gained experience with new technologies and services such as Auth0 and Twilio, delved deeper into MATLAB for data analysis, and enhanced our Python programming skills.

# What's Next for 1EAT
We aim to test our tool with real companies and their data to see how it can improve their annual profits and reduce their carbon footprint. We also plan to enhance the code to ensure it is maintainable by other developers. Additionally, we should consider expanding beyond Python and exploring other managed languages with frameworks such as Electron in Node.js, enabling the web app to function in a desktop environment and improving language accessibility.

https://devpost.com/software/1eat
