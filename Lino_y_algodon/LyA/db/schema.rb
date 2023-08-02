# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2023_07_14_002147) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "pregunta", force: :cascade do |t|
    t.bigint "producto_id", null: false
    t.text "texto"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id", null: false
    t.index ["producto_id"], name: "index_pregunta_on_producto_id"
    t.index ["user_id"], name: "index_pregunta_on_user_id"
  end

  create_table "productos", force: :cascade do |t|
    t.string "nombre"
    t.text "descripcion"
    t.integer "precio"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "responses", force: :cascade do |t|
    t.string "texto"
    t.bigint "pregunta_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["pregunta_id"], name: "index_responses_on_pregunta_id"
  end

  create_table "respuesta", force: :cascade do |t|
    t.string "texto"
    t.bigint "pregunta_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["pregunta_id"], name: "index_respuesta_on_pregunta_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "role"
    t.string "name"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "pregunta", "productos"
  add_foreign_key "pregunta", "users"
  add_foreign_key "responses", "pregunta", column: "pregunta_id"
  add_foreign_key "respuesta", "pregunta", column: "pregunta_id"
end
