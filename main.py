## from fastapi import FastAPI
# from scraper import fetch_opportunities
# from extractor import extract_data
# from categorizer import categorize_opportunity
# from database import save_opportunity

# from fastapi import Depends
# from sqlalchemy.orm import Session
# from database import get_db


# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Opportunity Tracker API running"}

# @app.post("/discover")
# def discover_opportunities():
#     raw_data = fetch_opportunities()
#     structured = [extract_data(item) for item in raw_data]
#     categorized = [categorize_opportunity(op) for op in structured]
#     for op in categorized:
#         save_opportunity(op)
#     return {"status": "success", "count": len(categorized)}

# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session

# from scraper import fetch_opportunities
# from extractor import extract_data
# from categorizer import categorize_opportunity
# from database import save_opportunity, get_db
# from models import Opportunity

## app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Opportunity Tracker API running"}

# @app.post("/discover")
# def discover_opportunities(db: Session = Depends(get_db)):
#     # Step 1: Scrape raw data
#     raw_data = fetch_opportunities()

#     # Step 2: Extract structured info
#     structured = [extract_data(item) for item in raw_data]

#     # Step 3: Categorize each opportunity
#     categorized = [categorize_opportunity(op) for op in structured]

#     # Step 4: Save into database
#     for op in categorized:
#         opportunity = Opportunity(
#             title=op.get("title"),
#             description=op.get("description"),
#             category=op.get("category")
#         )
#         save_opportunity(opportunity, db)

#     return {"status": "success", "count": len(categorized)}

## from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import get_db, save_opportunity
# from models import Opportunity
# from scraper import fetch_opportunities
# from categorizer import categorize


## app = FastAPI()

# @app.get("/discover")
# def discover_opportunities(db: Session = Depends(get_db)):
#     opportunities = fetch_opportunities()

#     for opp in opportunities:
#         new_opp = Opportunity(
#             title=opp["title"],
#             description="",   # अभी खाली
#             category=""       # बाद में categorizer से भरेंगे
#         )
#         save_opportunity(new_opp, db)   # <-- यहीं call करना है

#     return {"message": f"Inserted {len(opportunities)} opportunities"}


# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import get_db, save_opportunity
# from models import Opportunity
# from scraper import fetch_opportunities
# from categorizer import categorize

## app = FastAPI()

# @app.get("/discover")
# def discover_opportunities(db: Session = Depends(get_db)):
#     opportunities = fetch_opportunities()

#     for opp in opportunities:
#         # categorizer से category निकालें
#         category = categorize(opp["title"])
#         # scraper से description पहले से आ रहा है
#         description = opp.get("description", "")

#         new_opp = Opportunity(
#             title=opp["title"],
#             description=description,
#             category=category
#         )
#         save_opportunity(new_opp, db)

#     return {"message": f"Inserted {len(opportunities)} opportunities"}


# from fastapi import FastAPI, Depends
# from sqlalchemy import engine
# from sqlalchemy.orm import Session
# from database import Base, get_db, save_opportunity
# from models import Opportunity
# from scraper import fetch_opportunities
# from categorizer import categorize

# app = FastAPI()

# @app.get("/discover")
# def discover_opportunities(db: Session = Depends(get_db)):
#     opportunities = fetch_opportunities()

#     for opp in opportunities:
#         category = categorize(opp["title"])
#         description = opp.get("description", "")

#         new_opp = Opportunity(
#             title=opp["title"],
#             description=description,
#             category=category
#         )
#         save_opportunity(new_opp, db)

#     return {"message": f"Inserted {len(opportunities)} opportunities"}

# @app.get("/list")
# def list_opportunities(db: Session = Depends(get_db)):
#     opportunities = db.query(Opportunity).all()
#     return opportunities

# # नया search endpoint
# @app.get("/search")
# def search_opportunities(
#     category: str = None,
#     keyword: str = None,
#     db: Session = Depends(get_db)
# ):
#     query = db.query(Opportunity)

#     if category:
#         query = query.filter(Opportunity.category.ilike(f"%{category}%"))
#     if keyword:
#         query = query.filter(Opportunity.title.ilike(f"%{keyword}%"))

#     results = query.all()
#     return results

# @app.get("/")
# def root():
#     return {"message": "Backend is running"}


# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import Base, get_db, save_opportunity
# from models import Opportunity
# from scraper import fetch_opportunities
# from categorizer import categorize

# app = FastAPI()

# # @app.get("/discover")
# # def discover_opportunities(db: Session = Depends(get_db)):
# #     opportunities = fetch_opportunities()
# #     for opp in opportunities:
# #         category = categorize(opp["title"])
# #         description = opp.get("description", "")
# #         new_opp = Opportunity(
# #             title=opp["title"],
# #             description=description,
# #             category=category
# #         )
# #         save_opportunity(new_opp, db)
# #     return {"message": f"Inserted {len(opportunities)} opportunities"}

# @app.get("/discover")
# def discover_opportunities(db: Session = Depends(get_db)):
#     opportunities = fetch_opportunities()
#     for opp in opportunities:
#         status = categorize(opp["title"])   # पहले category था, अब status
#         description = opp.get("description", "")

#         new_opp = Opportunity(
#             title=opp["title"],
#             description=description,
#             country=opp.get("country", "Unknown"),
#             deadline=opp.get("deadline", None),
#             status=status
#         )
#         save_opportunity(new_opp, db)

#     return {"message": f"Inserted {len(opportunities)} opportunities"}


# @app.get("/list")
# def list_opportunities(db: Session = Depends(get_db)):
#     opportunities = db.query(Opportunity).all()
#     return opportunities

# @app.get("/search")
# def search_opportunities(
#     category: str = None,
#     keyword: str = None,
#     db: Session = Depends(get_db)
# ):
#     query = db.query(Opportunity)
#     if category:
#         query = query.filter(Opportunity.category.ilike(f"%{category}%"))
#     if keyword:
#         query = query.filter(Opportunity.title.ilike(f"%{keyword}%"))
#     results = query.all()
#     return results

# @app.get("/")
# def root():
#     return {"message": "Backend is running"}

# # 🔹 नया endpoint: frontend के लिए
# # @app.get("/api/opportunities")
# # def api_opportunities(db: Session = Depends(get_db)):
# #     opportunities = db.query(Opportunity).all()
# #     return opportunities

# @app.get("/api/opportunities")
# def api_opportunities(db: Session = Depends(get_db)):
#     opportunities = db.query(Opportunity).all()
#     result = []
#     for opp in opportunities:
#         result.append({
#             "id": opp.id,
#             "title": opp.title,
#             "country": getattr(opp, "country", "Unknown"),
#             "deadline": getattr(opp, "deadline", "N/A"),
#             "status": opp.category  # category को status मान लो
#         })
#     return result


# @app.get("/api/recommendations")
# def api_recommendations():
#     # फिलहाल static data, बाद में AI से dynamic कर सकते हो
#     return [
#         {"title": "UNESCO Youth Fellowship"},
#         {"title": "Google AI Startup Program"},
#         {"title": "Women Techmakers Scholarship"},
#     ]


from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, get_db, save_opportunity, engine
from models import Opportunity
from scraper import fetch_opportunities
from categorizer import categorize

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # React frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # सभी methods allow
    allow_headers=["*"],  # सभी headers allow
)


# Ensure tables are created
Base.metadata.create_all(bind=engine)

@app.get("/discover")
def discover_opportunities(db: Session = Depends(get_db)):
    opportunities = fetch_opportunities()
    for opp in opportunities:
        status = categorize(opp["title"])   # अब status field में डालें
        description = opp.get("description", "")

        new_opp = Opportunity(
            title=opp["title"],
            description=description,
            country=opp.get("country", "Unknown"),
            deadline=opp.get("deadline", None),
            status=status
        )
        save_opportunity(new_opp, db)

    return {"message": f"Inserted {len(opportunities)} opportunities"}


@app.get("/list")
def list_opportunities(db: Session = Depends(get_db)):
    opportunities = db.query(Opportunity).all()
    return opportunities


@app.get("/search")
def search_opportunities(
    status: str = None,
    keyword: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Opportunity)
    if status:
        query = query.filter(Opportunity.status.ilike(f"%{status}%"))
    if keyword:
        query = query.filter(Opportunity.title.ilike(f"%{keyword}%"))
    results = query.all()
    return results


@app.get("/")
def root():
    return {"message": "Backend is running"}


# @app.get("/api/opportunities")
# def api_opportunities(db: Session = Depends(get_db)):
#     opportunities = db.query(Opportunity).all()
#     result = []
#     for opp in opportunities:
#         result.append({
#             "id": opp.id,
#             "title": opp.title,
#             "description": opp.description,
#             "country": getattr(opp, "country", "Unknown"),
#             "deadline": getattr(opp, "deadline", "N/A"),
#             "status": getattr(opp, "status", "N/A")
#         })
#     return result

@app.get("/api/opportunities")
def api_opportunities(db: Session = Depends(get_db)):
    opportunities = db.query(Opportunity).all()
    result = []

    if opportunities:  # ✅ अगर DB में data है
        for opp in opportunities:
            result.append({
                "id": opp.id,
                "title": opp.title,
                "description": opp.description,
                "country": getattr(opp, "country", "Unknown"),
                "deadline": getattr(opp, "deadline", "N/A"),
                "status": getattr(opp, "status", "N/A")
            })
    else:  # ✅ fallback static data
        result = [
            {
                "id": 1,
                "title": "EU Startup Accelerator",
                "organization": "European Commission",
                "deadline": "2024-05-25",
                "tags": ["AI", "Startup"],
                "status": "Saved"
            },
            {
                "id": 2,
                "title": "Women Entrepreneurs Grant",
                "organization": "Female Founders Initiative",
                "deadline": "2024-06-10",
                "tags": ["Women", "Funding"],
                "status": "Applied"
            },
            {
                "id": 3,
                "title": "Africa Tech Challenge",
                "organization": "Tech for Africa",
                "deadline": "2024-05-30",
                "tags": ["Africa", "Innovation"],
                "status": "Planning"
            }
        ]

    return result

@app.get("/api/recommendations")
def api_recommendations():
    # ✅ Combined static + upcoming recommendations
    return [
        {"title": "UNESCO Youth Fellowship"},
        {"title": "Google AI Startup Program"},
        {"title": "Women Techmakers Scholarship"},
        {"title": "AI Innovation Fund – Due in 3 Days"},
        {"title": "Global Youth Challenge – Due in 5 Days"}
    ]


# @app.get("/api/recommendations")
# def api_recommendations():
#     # फिलहाल static data, बाद में AI से dynamic कर सकते हो
#     return [
#         {"title": "UNESCO Youth Fellowship"},
#         {"title": "Google AI Startup Program"},
#         {"title": "Women Techmakers Scholarship"},
#     ]
